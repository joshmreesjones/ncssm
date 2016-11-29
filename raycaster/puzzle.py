import pygame, sys, random
from pygame.locals import *

# Start pygame
pygame.init()

# Set dimension constants
FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 512
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
# Make sure we have an even number of boxes
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs an even number of boxes.'
XMARGIN = int((WINDOWWIDTH - ((BOARDWIDTH * BOXSIZE) + (GAPSIZE * (BOARDWIDTH - 1)))) / 2)
YMARGIN = int((WINDOWHEIGHT - ((BOARDHEIGHT * BOXSIZE) + (GAPSIZE * (BOARDHEIGHT - 1)))) / 2)

# Colors     R    G    B
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
BLUE     = (  0,   0, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BGCOLOR = NAVYBLUE
BOXCOLOR = WHITE

# Define shape constants
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

# Define what shapes and colors to use
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert (len(ALLCOLORS) * len(ALLSHAPES)) * 2 >= BOARDWIDTH * BOARDHEIGHT, 'Not enough shapes and colors to fill board'

def main():
    global DISPLAYSURF
    # Create window instantiate drawing surface, set up FPS clock
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Memory Puzzle')
    FPSCLOCK = pygame.time.Clock()

    # Instantiate the font object
    font = pygame.font.Font('BebasNeue.otf', 48)
    textSurface = font.render('Memory Puzzle', True, WHITE)
    textRect = textSurface.get_rect()
    textRect.center = (WINDOWWIDTH / 2, YMARGIN / 2)

    # Generate board and revealed boxes data
    board = generateBoard()
    revealedBoxes = generateRevealedBoxes()

    while True:
        # Draw background
        DISPLAYSURF.fill(BGCOLOR)

        # Draw board
        drawBoard(board, revealedBoxes)

        # Draw text
        DISPLAYSURF.blit(textSurface, textRect)

        # Event handling
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        # Draw highlights, if any
        if getBoxAtPixel(mousex, mousey) != None:
            boxx, boxy = getBoxAtPixel(mousex, mousey)
            if not revealedBoxes[boxx][boxy]:
                drawHighlight(boxx, boxy)
        if getBoxAtPixel(mousex, mousey) != None and mouseClicked:
            


        pygame.display.update()
        FPSCLOCK.tick(FPS)

def getBoxCoords(boxx, boxy):
    topLeftX = XMARGIN + (boxx * (BOXSIZE + GAPSIZE))
    topLeftY = YMARGIN + (boxy * (BOXSIZE + GAPSIZE))
    return (topLeftX, topLeftY)

def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            coordX, coordY = getBoxCoords(boxx, boxy)
            boxRect = pygame.Rect(coordX, coordY, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return None

def generateBoard():
    icons = []
    for shape in ALLSHAPES:
        for color in ALLCOLORS:
            icons.append((shape, color))
    random.shuffle(icons)
    iconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2)
    icons = icons[:iconsUsed] * 2
    random.shuffle(icons)
    
    board = []
    for i in range(BOARDWIDTH):
        column = []
        for j in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board

def generateRevealedBoxes():
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([False] * BOARDHEIGHT)
    return revealedBoxes

def drawHighlight(boxx, boxy):
    coordX, coordY = getBoxCoords(boxx, boxy)
    highlightRect = pygame.Rect(coordX - 5, coordY - 5, BOXSIZE + 10, BOXSIZE + 10)
    pygame.draw.rect(DISPLAYSURF, BLUE, highlightRect, 4)

def drawIcon(shape, color, boxx, boxy):
    coordX, coordY = getBoxCoords(boxx, boxy)
    half = BOXSIZE / 2
    quarter = BOXSIZE / 4

    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (coordX + half, coordY + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, color, (coordX + half, coordY + half), quarter - 5)
    elif shape == SQUARE:
        squareRect = pygame.Rect(coordX + quarter, coordY + quarter, half, half)
        pygame.draw.rect(DISPLAYSURF, color, squareRect)
    elif shape == DIAMOND:
        diamondRect = pygame.Rect(coordX, coordY, BOXSIZE, BOXSIZE)
        pointsList = (diamondRect.midtop, diamondRect.midright, diamondRect.midbottom, diamondRect.midleft)
        pygame.draw.polygon(DISPLAYSURF, color, pointsList)
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (coordX, coordY + i), (coordX + i, coordY))
            pygame.draw.line(DISPLAYSURF, color, (coordX + i, coordY + BOXSIZE - 1), (coordX + BOXSIZE - 1, coordY + i))
    elif shape == OVAL:
        ovalRect = pygame.Rect(coordX, coordY + quarter, BOXSIZE, half)
        pygame.draw.ellipse(DISPLAYSURF, color, ovalRect)

def drawBoard(board, revealed):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            if revealed[boxx][boxy]:
                shape = board[boxx][boxy][0]
                color = board[boxx][boxy][1]
                drawIcon(shape, color, boxx, boxy)
            else:
                coordX, coordY = getBoxCoords(boxx, boxy)
                coverRect = pygame.Rect(coordX, coordY, BOXSIZE, BOXSIZE)
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, coverRect)

main()
