import random
import time

import pygame

intSnakeSpeed = 10

INT_WINDOW_X = 720
INT_WINDOW_Y = 480

COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_WHITE = pygame.Color(255, 255, 255)
COLOR_RED = pygame.Color(255, 0, 0)
COLOR_GREEN = pygame.Color(0, 255, 0)
COLOR_BLUE = pygame.Color(0, 0, 255)

pygame.init()
pygame.display.set_caption("Snake à la Niederstetten")
GAME_WINDOW = pygame.display.set_mode((INT_WINDOW_X, INT_WINDOW_Y))

FPS = pygame.time.Clock()

SNAKE_POSITION = [100, 50]
SNAKE_BODY = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

arrFruitPosition = [
    random.randrange(1, (INT_WINDOW_X // 10)) * 10,
    random.randrange(1, (INT_WINDOW_Y // 10)) * 10
]
isFruitSpawned = True

strDirection = "RIGHT"
strChangeTo = strDirection

intScore = 0

def showScore(aChoice, aColor, aFont, aSize):
    scoreFont = pygame.font.SysFont(aFont, aSize)
    scoreSurface = scoreFont.render("Score: " + str(intScore), True, aColor)
    scoreRect = scoreSurface.get_rect()
    GAME_WINDOW.blit(scoreSurface, scoreRect)

def gameOver():
    myFont = pygame.font.SysFont('times new roman', 50)
    gameOverSurface = myFont.render("Your Score is: " + str(intScore), True, COLOR_RED)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (INT_WINDOW_X / 2, INT_WINDOW_Y / 4)
    GAME_WINDOW.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:

    for anEvent in pygame.event.get():
        if anEvent.type == pygame.KEYDOWN:
            if anEvent.key == pygame.K_w:
                strChangeTo = "UP"
            if anEvent.key == pygame.K_s:
                strChangeTo = "DOWN"
            if anEvent.key == pygame.K_a:
                strChangeTo = "LEFT"
            if anEvent.key == pygame.K_d:
                strChangeTo = "RIGHT"

    if strChangeTo == 'UP' and strDirection != 'DOWN':
        strDirection = 'UP'
    if strChangeTo == 'DOWN' and strDirection != 'UP':
        strDirection = 'DOWN'
    if strChangeTo == 'LEFT' and strDirection != 'RIGHT':
        strDirection = 'LEFT'
    if strChangeTo == 'RIGHT' and strDirection != 'LEFT':
        strDirection = 'RIGHT'

    if strDirection == "UP":
        SNAKE_POSITION[1] -= 10
    if strDirection == "DOWN":
        SNAKE_POSITION[1] += 10
    if strDirection == "LEFT":
        SNAKE_POSITION[0] -= 10
    if strDirection == "RIGHT":
        SNAKE_POSITION[0] += 10

    SNAKE_BODY.insert(0, list(SNAKE_POSITION))
    if SNAKE_POSITION[0] == arrFruitPosition[0] and SNAKE_POSITION[1] == arrFruitPosition[1]:
        intScore += 10
        isFruitSpawned = False
    else:
        SNAKE_BODY.pop()

    if not isFruitSpawned:
        arrFruitPosition = [
            random.randrange(1, (INT_WINDOW_X // 10)) * 10,
            random.randrange(1, (INT_WINDOW_Y // 10)) * 10
        ]

    isFruitSpawned = True
    GAME_WINDOW.fill(COLOR_BLACK)

    for aPos in SNAKE_BODY:
        pygame.draw.rect(GAME_WINDOW, COLOR_GREEN, pygame.Rect(
            aPos[0], aPos[1], 10, 10
        ))

    pygame.draw.rect(GAME_WINDOW, COLOR_WHITE, pygame.Rect(
        arrFruitPosition[0], arrFruitPosition[1], 10, 10
    ))

    if SNAKE_POSITION[0] < 0 or SNAKE_POSITION[0] > INT_WINDOW_X - 10:
        gameOver()
    if SNAKE_POSITION[1] < 0 or SNAKE_POSITION[1] > INT_WINDOW_Y - 10:
        gameOver()

    for aBlock in SNAKE_BODY[1:]:
        if SNAKE_POSITION[0] == aBlock[0] and SNAKE_POSITION[1] == aBlock[1]:
            gameOver()

    showScore(1, COLOR_WHITE, "times new roman", 20)

    pygame.display.update()

    FPS.tick(intSnakeSpeed)


