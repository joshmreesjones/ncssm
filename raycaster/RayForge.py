import sys
import os
import pygame
import random
import math
from pygame.locals import *
#try:
    #from Numeric import *
    #import pygame.surfarray as surfarray
#except ImportError:
    #raise ImportError, "Numeric and Surfarray are required."
progpath=os.getcwd()+"/"
keys=[False]*324

def group(array, howmany):
    """Turns a 1D list into a 2D list"""
    i=0
    tmp=[]
    while i<len(array):
        tmp.extend([[array[i+j] for j in range(howmany)]])
        i+=howmany
    return tmp

mapgrid=[1,1,1,1,1,
         1,0,0,0,1,
         1,0,2,0,1,
         1,0,2,0,1,
         1,1,1,1,1]

heightgrid=[1,2,.5,.75,2,
         1,0,0,0,1,
         1,0,.25,0,1,
         1,0,.25,0,1,
         1,.25,1,.25,1]

mapgrid=group(mapgrid,5)
heightgrid=group(heightgrid,5)

def blitPartial(src,dest, destcoord,srcrect):
    dest.blit(src,destcoord,pygame.Rect(srcrect))

def kill():       
    pygame.display.quit()
    pygame.quit()
    return

def main():
    pygame.init()
    pygame.font.init()
    w=320.0
    h=200.0
    screen=pygame.display.set_mode((int(w*2),int(h)),pygame.SWSURFACE|pygame.DOUBLEBUF,24)#|pygame.FULLSCREEN,24)
    pygame.display.set_caption("RayForge")
    clock=pygame.time.Clock()
    posx,posy=1.5,3.5
    dirx,diry=1.0,0.0
    planex,planey=0.0,0.66
    mapboundx=5
    mapboundy=5
    rotspeed=.05
    movespeed=.025
    resolution=2 #LINES PER SLICE

    #TRIG CONSTANTS
    invcosrot=math.cos(-rotspeed)
    invsinrot=math.sin(-rotspeed)
    cosrot=math.cos(rotspeed)
    sinrot=math.sin(rotspeed)
    while True:
        #INPUT HANDLING AND THROTTLING
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==QUIT:
                kill()
                return
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    kill()
                    return
                keys[event.key]=True
            elif event.type==KEYUP: 
                keys[event.key]=False
                
        #CLEARING AND FLOOR
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(92,92,92),(w,h/2,w,h))

        x=0
        while x<w:            
            #INITIAL SETUP
            camerax=2.0*x/w-1.0
            rayposx,rayposy=posx,posy
            raydirx=dirx+planex*camerax
            raydiry=diry+planey*camerax+.000000000000001
            mapx,mapy=int(rayposx),int(rayposy)
            deltadistx=math.sqrt(1.0+(raydiry*raydiry)/(raydirx*raydirx))
            deltadisty=math.sqrt(1.0+(raydirx*raydirx)/(raydiry*raydiry))
            zbuffer=[]
            
            #CONSTANT DEFINITION
            if raydirx<0:
                stepx=-1
                sidedistx=(rayposx-mapx)*deltadistx
            else:
                stepx=1
                sidedistx=(mapx+1.0-rayposx)*deltadistx
                
            if raydiry<0:
                stepy=-1
                sidedisty=(rayposy-mapy)*deltadisty
            else:
                stepy=1
                sidedisty=(mapy+1.0-rayposy)*deltadisty

            #DIGITAL DIFFERENTIAL ANALYSIS
            while 1:
                if sidedistx<sidedisty:
                    sidedistx+=deltadistx
                    mapx+=stepx
                    side=0
                else:
                    sidedisty+=deltadisty
                    mapy+=stepy
                    side=1
                if mapx>=mapboundx or mapx<0 or mapy>=mapboundy or mapy<0 or len(zbuffer)==5:
                    break
                elif mapgrid[mapx][mapy]>0:
                    zbuffer.append([mapx,mapy,stepx,stepy,side,heightgrid[mapx][mapy]])
            #ZBUFFER DRAWING   
            zbuffer=zbuffer[::-1]
            for i in zbuffer:
                if i[4]==0:
                    wallheight=abs((i[0]-rayposx+(1.0-i[2])/2.0)/raydirx)
                else:
                    wallheight=abs((i[1]-rayposy+(1.0-i[3])/2.0)/raydiry)
                lineheight=abs(int(h/(wallheight+.0000001)))                
                top=-(lineheight*i[5])/2.0+h/2.0
                bottom=lineheight/2.0+h/2.0
                if top<0:top=0
                if bottom>=h:bottom=h-1
                
                #RENDERING & COLOR
                c=255.0-abs(int(wallheight*32))*1.5
                if c<1:c=0
                if c>255:c=255
                
                #SIMPLEST LIGHTING EVER!
                if i[4]: c*=.75
                
                pygame.draw.line(screen,(c,c,c),(x,top),(x,bottom),resolution)               
                    
            x+=resolution
        
        #MAP UPDATE
        x=0
        while x<=w:
            pygame.draw.line(screen,(255,255,255),(x+320,0),(x+320,h),2)
            x+=(w/mapboundx)
        y=0
        while y<=h:
            pygame.draw.line(screen,(255,255,255),(0+320,y),(w+320,y),2)
            y+=(h/mapboundy)
        mx=0
        while mx<mapboundx:
            my=0
            while my<mapboundy:
                c=127*heightgrid[mx][my]
                pygame.draw.rect(screen,(c,c,c),(mx*(w/mapboundx)+2+320,my*(h/mapboundy)+2,(w/mapboundx)-2,(h/mapboundy)-2))
                my+=1
            mx+=1
    
        pygame.draw.rect(screen,(0,255,0),(posx*(w/mapboundx)-2+320,posy*(h/mapboundy)-2,4,4))
        pygame.draw.line(screen,(255,0,127),(posx*(w/mapboundx)+320,posy*(h/mapboundy)),((dirx+posx+planex)*(w/mapboundx)+320,(diry+posy+planey)*(h/mapboundy)))
        pygame.draw.line(screen,(255,0,127),(posx*(w/mapboundx)+320,posy*(h/mapboundy)),((dirx+posx-planex)*(w/mapboundx)+320,(diry+posy-planey)*(h/mapboundy)))
        pygame.draw.line(screen,(255,0,127),((dirx+posx+planex)*(w/mapboundx)+320,(diry+posy+planey)*(h/mapboundy)),((dirx+posx-planex)*(w/mapboundx)+320,(diry+posy-planey)*(h/mapboundy)))
        
        #VECTOR MANIPULATION
        if keys[K_w]:
            if not mapgrid[int(posx+dirx*movespeed)][int(posy)]: posx += (dirx) * movespeed
            if not mapgrid[int(posx)][int(posy+diry*movespeed)]: posy += (diry) * movespeed

        if keys[K_s]:
            if not mapgrid[int(posx-dirx*movespeed)][int(posy)]: posx -= (dirx) * movespeed
            if not mapgrid[int(posx)][int(posy-diry*movespeed)]: posy -= (diry) * movespeed
         
        if keys[K_d]:
            old=dirx
            dirx=dirx*cosrot-diry*sinrot
            diry=old*sinrot+diry*cosrot
            old=planex
            planex=planex*cosrot-planey*sinrot
            planey=old*sinrot+planey*cosrot
            
        if keys[K_a]:
            old=dirx
            dirx=dirx*invcosrot-diry*invsinrot
            diry=old*invsinrot+diry*invcosrot
            old=planex
            planex=planex*invcosrot-planey*invsinrot
            planey=old*invsinrot+planey*invcosrot
        pygame.display.flip()
    return

if __name__=="__main__": main()
