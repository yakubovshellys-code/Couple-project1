import random
import pygame

GRASS_AMOUNT = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRASS_WIDTH = 30
GRASS_HEIGHT = 30
SOLIDER_WIDTH = 50
SOLIDER_HEIGHT = 50

def solider_location(screen,location):
    solider_image = pygame.image.load('soldier.png')
    solider_image = pygame.transform.scale(solider_image, (SOLIDER_WIDTH, SOLIDER_HEIGHT))
    screen.blit(solider_image, location)

def add_grass():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Random Grass")
    screen.fill(pygame.Color('green'))
    grass_image = pygame.image.load('grass.png')
    grass_image = pygame.transform.scale(grass_image, (GRASS_WIDTH, GRASS_HEIGHT))
    for element in range(GRASS_AMOUNT):
        x = random.randint(0, SCREEN_WIDTH - GRASS_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT - GRASS_HEIGHT)
        screen.blit(grass_image, (x, y))
    solider_location(screen, (0, 0))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

add_grass()

