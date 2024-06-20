import pygame
import random

# Init pygame
pygame.init()

# Create a screen
height = 600
width = 600
screen = pygame.display.set_mode((width, height))

# Set icon and screen name
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon-stars.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("player.png")
playerX = width / 2 - 40
playerY = height - 100
playerXChange = 0
playerYChange = 0

# Enemy
enemyImage = pygame.image.load("enemy.png")
enemyX = random.randint(0, (width - 40))
enemyY = random.randint(0, (width // 2))
enemyXChange = 0.3
enemyYChange = 40


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y):
    screen.blit(enemyImage, (x, y))


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange = -0.2
            if event.key == pygame.K_RIGHT:
                playerXChange = 0.2

            # if event.key == pygame.K_UP:
            #    playerYChange = -0.2
            # if event.key == pygame.K_DOWN:
            #    playerYChange = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerYChange = 0

    playerX += playerXChange
    playerY += playerYChange

    # Player movement boundary
    if playerX < 0:
        playerX = 0
    elif playerX >= width - 80:
        playerX = width - 80

    if playerY < 0:
        playerY = 0
    elif playerY >= height - 80:
        playerY = height - 80

    # Enemy movement + boundary
    enemyX += enemyXChange

    if enemyX < 0:
        enemyXChange *= -1
        enemyY += enemyYChange
    elif enemyX >= width - 80:
        enemyXChange *= -1
        enemyY += enemyYChange

    # RGB in screen
    red = 0
    green = 0
    blue = 0
    screen.fill((red, green, blue))

    # playerX += 1

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
