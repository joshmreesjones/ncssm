import pygame, sys, math
from pygame.locals import *
pygame.init()

windowWidth = 512
windowHeight = 384

FPS = 30
fpsClock = pygame.time.Clock()

pygame.key.set_repeat(1, 1)

moveSpeed = .5
rotSpeed = .1

wallHeight = 1

#            R    G    B
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
BLACK    = (  0,   0,   0)
ORANGE   = (255, 128,   0)

mapColors = {
    1: RED,
    2: GREEN,
    3: BLUE,
    4: WHITE,
    5: ORANGE
}

# Used to make darker colors for y-side walls
def halfTuple(oldTuple):
    return tuple(x * 0.5 for x in oldTuple)

darkMapColors = {
    1: halfTuple(RED),
    2: halfTuple(GREEN),
    3: halfTuple(BLUE),
    4: halfTuple(WHITE),
    5: halfTuple(ORANGE)
    
}

# Crude world map - generic 'shapes' to test game engine
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

# Dimensions in square 'wall' units
mapWidth = len(worldMap)
mapHeight = len(worldMap[0])

def main():
    # Create window
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Raycaster")

    # Define vectors: pos, dir, and plane
    posX = 22
    posY = 12

    dirX = -1
    dirY = 0

    planeX = 0
    planeY = .66

    # Main game loop
    while True:
        screen.fill(BLACK)
        for x in range(0, windowWidth):
            #print(x)
            # cameraX used to scale things
            cameraX = (2 * x / windowWidth) - 1

            # Define vectors for each ray 'sent out'
            rayPosX = posX
            rayPosY = posY

            rayDirX = dirX + (planeX * cameraX)
            rayDirY = dirY + (planeY * cameraX) + .0000000000001

            # Which map unit we're in
            mapX = int(posX)
            mapY = int(posY)

            deltaDistX = math.sqrt(1 + (rayDirY ** 2) / (rayDirX ** 2))
            deltaDistY = math.sqrt(1 + (rayDirX ** 2) / (rayDirY ** 2))
            # Credit to defining sideDistXY to my roommate Bradley King
            sideDistX = math.sqrt((abs(abs(rayPosX - mapX) - 1) ** 2) + (rayDirY ** 2) / (rayDirX ** 2))
            sideDistY = math.sqrt((abs(abs(rayPosY - mapY) - 1) ** 2) + (rayDirX ** 2) / (rayDirY ** 2))

            stepX = None
            stepY = None
            if rayPosX < 0:
                stepX = -1
            else:
                stepX = 1
            if rayPosY < 0:
                stepY = -1
            else:
                stepY = 1

            # Perform DDA - thanks Lode Vanderildeen
            side = None
            hit = False
            while not hit:
                if sideDistX < sideDistY:
                    sideDistX += deltaDistX
                    mapX += stepX
                    side = 0
                else:
                    sideDistY += deltaDistY
                    mapY += stepY
                    side = 1
                try:
                    if worldMap[mapX][mapY] > 0:
                        hit = True
                except:
                    continue

            # Calculate distance to next wall
            if side == 0:
                wallDist = sideDistX
            else:
                wallDist = sideDistY

            # Set line height
            lineHeight = abs(int(windowHeight / wallDist))

            # Set start of line and end of line
            lineStartY = (-lineHeight / 2) + (windowHeight / 2)
            if lineStartY < 0:
                lineStartY = 0
            lineStart = (x, (-lineHeight / 2) + (windowHeight / 2))
            lineEndY = (lineHeight / 2) + (windowHeight / 2)
            if lineEndY > windowHeight:
                lineEndY = windowHeight
            lineEnd = (x, (lineHeight / 2) + (windowHeight / 2))
            
            # Set color of line
            if side == 1:
                color = mapColors[worldMap[mapX][mapY]]
            else:
                color = darkMapColors[worldMap[mapX][mapY]]
            
            pygame.draw.line(screen, color, lineStart, lineEnd)

        # Update display, tick FPS clock
        pygame.display.update()
        fpsClock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif (event.type == KEYDOWN) and (event.key == K_s):
                print('w')
                try:
                    worldMap[int(posX + (dirX * moveSpeed))][int(posY)]
                    worldMap[int(posX)][int(posY + (dirY * moveSpeed))]
                    posX += dirX * moveSpeed
                    posY += dirY * moveSpeed
                except:
                    break
            elif (event.type == KEYDOWN) and (event.key == K_w):
                try:
                    worldMap[int(posX + (dirX * moveSpeed))][int(posY)]
                    worldMap[int(posX)][int(posY + (dirY * moveSpeed))]
                    posX -= dirX * moveSpeed
                    posY -= dirY * moveSpeed
                except:
                    break
            elif (event.type == KEYDOWN) and (event.key == K_d):
                oldDirX = dirX
                dirX = (dirX * math.cos(-rotSpeed)) + (dirY * math.sin(-rotSpeed))
                dirY = (-oldDirX * math.sin(-rotSpeed)) + (dirY * math.cos(-rotSpeed))
                oldPlaneX = planeX
                planeX = (planeX * math.cos(rotSpeed)) + (planeY * math.sin(rotSpeed))
                planeY = (-oldPlaneX * math.sin(rotSpeed)) + (planeY * math.cos(rotSpeed))
            elif (event.type == KEYDOWN) and (event.key == K_a):
                oldDirX = dirX
                dirX = (dirX * math.cos(-rotSpeed)) + (dirY * math.sin(-rotSpeed))
                dirY = (-oldDirX * math.sin(-rotSpeed)) + (dirY * math.cos(-rotSpeed))
                oldPlaneX = planeX
                planeX = (planeX * math.cos(-rotSpeed)) + (planeY * math.sin(-rotSpeed))
                planeY = (-oldPlaneX * math.sin(rotSpeed)) + (planeY * math.cos(rotSpeed))
            elif (event.type == KEYDOWN) and (event.key == K_RIGHT):
                posX += planeX * moveSpeed
                posY += planeY * moveSpeed
            elif (event.type == KEYDOWN) and (event.key == K_LEFT):
                posX -= planeX * moveSpeed
                posY -= planeY * moveSpeed

main()
