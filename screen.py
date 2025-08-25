import random
import pygame
from consts import *



def solider_location(screen,location):
    solider_image = pygame.image.load('soldier.png')
    solider_image = pygame.transform.scale(solider_image, (P_SOLIDER_WIDTH, P_SOLIDER_HEIGHT))
    screen.blit(solider_image, location)
def flag_location(screen,location):
    flag_image = pygame.image.load('flag.png')
    flag_image = pygame.transform.scale(flag_image, (P_FLAG_WIDTH, P_FLAG_HEIGHT))
    screen.blit(flag_image, location)
def add_grass():
    pygame.init()
    screen = pygame.display.set_mode((P_SCREEN_WIDTH, P_SCREEN_HEIGHT))
    screen.fill(pygame.Color('green'))
    grass_image = pygame.image.load('grass.png')
    grass_image = pygame.transform.scale(grass_image, (P_GRASS_WIDTH, P_GRASS_HEIGHT))
    for element in range(P_GRASS_AMOUNT):
        x = random.randint(0, P_SCREEN_WIDTH - P_GRASS_WIDTH)
        y = random.randint(0, P_SCREEN_HEIGHT - P_GRASS_HEIGHT)
        screen.blit(grass_image, (x, y))
    solider_location(screen, (0, 0))
    flag_x=P_SCREEN_WIDTH - P_FLAG_WIDTH
    flag_y=P_SCREEN_HEIGHT - P_FLAG_HEIGHT
    flag_location(screen, (flag_x, flag_y))
    sent=pygame.font.Font(None, 20)
    titles=sent.render('Welcome to the flag game.', True, (255, 255, 255))
    titles2=sent.render('Have fun!', True, (255, 255, 255))
    screen.blit(titles,(65,15))
    screen.blit(titles2,(65,25))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

add_grass()

