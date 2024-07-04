import pygame
import random
import math
from pygame import mixer

# General movement speed multiplier
speed = 4

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
numOfEnemies = 6

enemyImage = []
enemyX = []
enemyY = []
enemyXChange = []
enemyYChange = []

for e in range(numOfEnemies):
    enemyImage.append(pygame.image.load("img/enemy.png"))
    enemyX.append(random.randint(40, (width - 80)))
    enemyY.append(random.randint(40, (width // 3)))
    enemyXChange.append(0.4 * speed)
    enemyYChange.append(40)

# Bullet
bulletImage = pygame.image.load("img/bullet.png")
bulletX = playerX
bulletY = playerY
bulletYChange = -0.8 * speed
bulletState = "ready"

# Score
scoreValue = 0
font = pygame.font.Font("freesansbold.ttf", 20)
textX = 10
textY = 10

# Game Over Screen
over_font = pygame.font.Font("freesansbold.ttf", 80)

# Background sound
mixer.music.load("sound/background2.wav")
mixer.music.play(-1)


def gameOverText(x,y):
    overText = over_font.render("Game Over!", True, (255, 255, 255))
    screen.blit(overText, (x, y))
    overText = over_font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(overText, (x + 70, y + 70))


def showScore(x,y):
    score = font.render("Score: " + str(scoreValue), True,(255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y, e):
    screen.blit(enemyImage[e], (x, y))


def fireBullet(x):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImage, (x, bulletY))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(bulletX - enemyX, 2)) + (math.pow(bulletY - enemyY, 2)))

    if distance <= 60:
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
        # Quiting game
        if event.type == pygame.QUIT:
            running = False

        # General movement
        if event.type == pygame.KEYDOWN:
            # Player movement
            if event.key == pygame.K_LEFT:
                playerXChange = -0.4 * speed
            if event.key == pygame.K_RIGHT:
                playerXChange = 0.4 * speed

            # Bullet state to fire
            if event.key == pygame.K_SPACE:
                # updates bullet x position only when shoting
                if bulletState == "ready":
                    bulletX = playerX
                    fireBullet(bulletX + 18)
                    # fireBullet(bulletX + 52)

                    # Bullet sound
                    bulletSound = mixer.Sound("sound/laser2.wav")
                    bulletSound.play()

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
    for e in range(numOfEnemies):
        enemyX[e] += enemyXChange[e]

        if enemyX[e] < 0:
            enemyXChange[e] *= -1
            enemyY[e] += enemyYChange[e]
        elif enemyX[e] >= width - 80:
            enemyXChange[e] *= -1
            enemyY[e] += enemyYChange[e]

        # Collision
        collision = isCollision(enemyX[e], enemyY[e], bulletX, bulletY)
        if collision:
            # Resets bullet
            bulletState = "ready"
            bulletY = playerY

            # Resets enemy
            enemyX[e] = random.randint(40, (width - 80))
            enemyY[e] = random.randint(40, (width // 3))
            enemyXChange[e] *= -1

            scoreValue += 1

            # Enemy death sound
            enemyDeathSound = mixer.Sound("sound/explosion2.wav")
            enemyDeathSound.play()

        enemy(enemyX[e], enemyY[e], e)

        # Game Over
        if enemyY[e] > playerY - 60:
            for i in range(numOfEnemies):
                enemyY[i] = 2000
            gameOverText(width / 8, height / 3)
            mixer.music.fadeout(2000)
            # mixer.music.stop()
            break

    # Bullet movement
    if bulletY <= 0:
        bulletY = playerY
        bulletState = "ready"

    if bulletState == "fire":
        fireBullet(bulletX + 18)
        fireBullet(bulletX + 52)
        bulletY += bulletYChange

    player(playerX, playerY)

    showScore(textX,textY)

    pygame.display.update()
