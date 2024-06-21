import pygame
import random
import math

# Init pygame
pygame.init()

# Create a screen
height = 600
width = 600
screen = pygame.display.set_mode((width, height))

# Set icon and screen name
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("img/icon-stars.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("img/player.png")
playerX = width / 2 - 40
playerY = height - 100
playerXChange = 0
playerYChange = 0

# Enemy
enemyImage = pygame.image.load("img/enemy.png")
enemyX = random.randint(0, (width - 40))
enemyY = random.randint(0, (width // 3))
enemyXChange = 0.4
enemyYChange = 40

# Bullet
bulletImage = pygame.image.load("img/bullet.png")
bulletX = playerX
bulletY = playerY
bulletYChange = -0.8
bulletState = "ready"


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y):
    screen.blit(enemyImage, (x, y))


def fireBullet(x):
    global bulletState
    global bulletX
    bulletState = "fire"
    screen.blit(bulletImage, (x, bulletY))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(bulletX - enemyX), 2) + (math.pow(bulletY - enemyY), 2))

    if distance < 20:
        return True
    else:
        return False


# Game loop
running = True
while running:
    # RGB in screen
    red = 0
    green = 0
    blue = 0
    screen.fill((red, green, blue))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # General movement
        if event.type == pygame.KEYDOWN:
            # Player movement
            if event.key == pygame.K_LEFT:
                playerXChange = -0.4
            if event.key == pygame.K_RIGHT:
                playerXChange = 0.4

            # Bullet state to fire
            if event.key == pygame.K_SPACE:
                # updates bullet x position only when shoting
                if bulletState == "ready":
                    bulletX = playerX

                fireBullet(bulletX + 18)
                fireBullet(bulletX + 52)

        # Player movement
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

    # Bullet movement
    if bulletY <= 0:
        bulletY = playerY
        bulletState = "ready"

    if bulletState == "fire":
        fireBullet(bulletX + 18)
        fireBullet(bulletX + 52)
        bulletY += bulletYChange

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
