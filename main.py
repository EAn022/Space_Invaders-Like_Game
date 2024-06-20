import pygame

# Init pygame
pygame.init()

# Create a screen
height = 400
width = 600
screen = pygame.display.set_mode((width, height))

# Set icon and screen name
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon-stars.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("player.png")
playerX = 270
playerY = 300
playerXChange = 0
playerYChange = 0


def player(x, y):
    screen.blit(playerImage, (x, y))


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange = -0.2
            if event.key == pygame.K_RIGHT:
                playerXChange = 0.2

            if event.key == pygame.K_UP:
                playerYChange = -0.2
            if event.key == pygame.K_DOWN:
                playerYChange = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerYChange = 0

    playerX += playerXChange
    playerY += playerYChange


    # RGB in screen
    red = 0
    green = 0
    blue = 0
    screen.fill((red, green, blue))

    # playerX += 1

    player(playerX, playerY)
    pygame.display.update()
