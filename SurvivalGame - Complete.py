import pygame
import random
from Player import Player
from Enemy import Enemy
from Text import Text

pygame.init()

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("")
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

# IMPORT IMAGES:
jimmyImage = pygame.image.load("_images/jimmy.png")
enemyImage = pygame.image.load("_images/Enemy.png")

# CREATING SPRITE GROUPS:
allSprites = pygame.sprite.Group()
enemySprites = pygame.sprite.Group()

# CREATING OBJECTS:
player = Player(50, jimmyImage, 0.25, 30, screenHeight -
                30, screenWidth, screenHeight, 3)
enemy1 = Enemy(50, enemyImage, 0.25, random.randint(
    int(screenWidth/2), screenWidth), random.randint(0, screenHeight), 3, player)

# ADD OBJECTS TO GROUPS:
allSprites.add(player)
allSprites.add(enemy1)

enemySprites.add(enemy1)

time = 0
reset = 0
game_state = "Play"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if game_state == "Lose":
        # BLIT GAMEOVER BACKGROUND TO SCREEN
        screen.fill(black)
        gameOverText = Text(screen, "GAME OVER - Score:" +
                            str(time), 30, white, screenWidth/2, screenHeight/2)
        gameOverText.draw()

    else:

        screen.fill(white)

        # Collisions Here
        hitList = pygame.sprite.spritecollide(player, enemySprites, False)

        for hit in hitList:
            game_state = "Lose"

        # TIMER FOR PLAYER:
        time = pygame.time.get_ticks()/1000

        # Draw Text for correct time:
        gameTimeText = Text(screen, "Time:" + str(time),
                            30, black, screenWidth/2, 30)
        gameTimeText.draw()

        # TEN SECOND TIMER FOR ENEMY:
        milliseconds = pygame.time.get_ticks() - reset
        if milliseconds >= 10000:
            reset += 10000
            enemy = Enemy(50, enemyImage, 0.25, random.randint(
                int(screenWidth/2), screenWidth), random.randint(0, screenHeight), 3, player)
            allSprites.add(enemy)
            enemySprites.add(enemy)

        # Increase enemy sprite speed over time
        for enemy in enemySprites:
            enemy.speed = max(1, time/15)

        # UPDATE GROUPS:
        allSprites.update()

        # DRAWING TO SCREEN:
        allSprites.draw(screen)

    clock.tick(40)
    pygame.display.update()
