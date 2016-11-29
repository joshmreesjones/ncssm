import pygame, sys, math
from pygame.locals import *
pygame.init()

mapWidth = 24
mapHeight = 24

windowWidth = 512
windowHeight = 384

FPS = 30
fpsClock = pygame.time.Clock()

pygame.key.set_repeat(1, 1)

moveSpeed = .5
rotSpeed = .5

#            R    G    B
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
BLACK    = (  0,   0,   0)

mapColors = {
    1: RED,
    2: GREEN,
    3: BLUE,
    4: WHITE
}

def halfTuple(oldTuple):
    newList = []
    for item in oldTuple:
        newList.append(item * .75)
    return tuple(newList)

darkMapColors = {
    1: halfTuple(RED),
    2: halfTuple(GREEN),
    3: halfTuple(BLUE),
    4: halfTuple(WHITE)
}

worldMap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 0, 5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def main():
    posX = 22
    posY = 12

    dirX = -1
    dirY = 0

    planeX = 0
    planeY = .66
    time = 0
    oldTime = 0

    screen = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
    pygame.display.set_caption("Raycaster")

    while True: # main game loop
        for x in range(windowWidth):
            cameraX = ((2 * x) / windowWidth) - 1 # [-1:1]
            rayPosX = posX
            rayPosY = posY
            rayDirX = dirX + (planeX * cameraX)
            rayDirY = dirY + (planeY * cameraX)

            mapX = int(rayPosX)
            mapY = int(rayPosY)

            sideDistX = None
            sideDistY = None
            #print("(",posX, posY,") (",dirX, dirY,") (",rayDirX, rayDirY,")")
            if rayDirY == 0:
                print("AGGG")
                continue
            deltaDistX = math.sqrt(1 + (rayDirY ** 2) / (rayDirX * rayDirY))
            deltaDistY = math.sqrt(1 + (rayDirX ** 2) / (rayDirY * rayDirY))

            perpWallDist = None

            stepX = None
            stepY = None

            hit = 0
            side = None

            if rayDirX < 0:
                stepX = -1
                sideDistX = (rayPosX - mapX) * deltaDistX
            else:
                stepX = 1
                sideDistX = (mapX + 1 - rayPosX) * deltaDistX

            if rayDirY < 0:
                stepY = -1
                sideDistY = (rayPosY - mapY) * deltaDistY
            else:
                stepY = 1
                sideDistY = (mapY + 1 - rayPosY) * deltaDistY

            while hit == 0:
                if sideDistX < sideDistY:
                    sideDistX += deltaDistX
                    mapX += stepX
                    side = 0
                else:
                    sideDistY += deltaDistY
                    mapY += stepY
                    side = 1

                if worldMap[mapX][mapY] > 0:
                    hit = 1

            if side == 0:
                perpWallDist = abs((mapX - rayPosX + (1 - stepX) / 2) / rayDirX)
            else:
                perpWallDist = abs((mapY - rayPosY + (1 - stepY) / 2) / rayDirY)

            lineHeight = abs(int(windowHeight / perpWallDist))

            drawStart = -(lineHeight / 2) + (windowHeight / 2)
            drawEnd = (lineHeight / 2) + (windowHeight / 2)

            if drawStart < 0:
                drawStart = 0
            if drawEnd >= windowHeight:
                drawEnd = windowHeight - 1

            color = None

            color = mapColors[worldMap[mapX][mapY]]

            if side == 1:
                color = darkMapColors[worldMap[mapX][mapY]]

            pygame.draw.line(screen, color, (x, drawStart), (x, drawEnd), 1)

        oldTime = time
        time = pygame.time.get_ticks()
        frameTime = (time - oldTime) / 1000

        pygame.display.update()
        fpsClock.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == KEYDOWN) and (event.key == K_UP):
                if worldMap[int(posX + dirX * moveSpeed)][int(posY)] == False:
                    posX += dirX * moveSpeed
                if worldMap[int(posX)][int(posY - dirY * moveSpeed)] == False:
                    posY += dirY * moveSpeed
            elif (event.type == KEYDOWN) and (event.key == K_DOWN):
                if worldMap[int(posX - dirX * moveSpeed)][int(posY)] == False:
                    posX -= dirX * moveSpeed
                if worldMap[int(posX)][int(posY - dirY * moveSpeed)] == False:
                    posY -= dirY * moveSpeed
            elif (event.type == KEYDOWN) and (event.key == K_RIGHT):
                oldDirX = dirX
                dirX = dirX * math.cos(-rotSpeed) - dirY * math.sin(-rotSpeed)
                dirY = oldDirX * math.sin(-rotSpeed) + dirY * math.cos(-rotSpeed)
                oldPlaneX = planeX
                planeX = planeX * math.cos(-rotSpeed) - planeY * math.sin(-rotSpeed)
                planeY = oldPlaneX * math.sin(-rotSpeed) + planeY * math.cos(-rotSpeed)
            elif (event.type == KEYDOWN) and (event.key == K_LEFT):
                print('yay')

main()
