import random
import pygame
from consts import *
import time


def draw_solider(screen, location):
    solider_image = pygame.image.load('soldier.png')
    solider_image = pygame.transform.scale(solider_image, (P_SOLIDER_WIDTH, P_SOLIDER_HEIGHT))
    screen.blit(solider_image, location)


def draw_flag(screen, location):
    flag_image = pygame.image.load('flag.png')
    flag_image = pygame.transform.scale(flag_image, (P_FLAG_WIDTH, P_FLAG_HEIGHT))
    screen.blit(flag_image, location)


def draw_grass(screen):
    grass_image = pygame.image.load('grass.png')
    grass_image = pygame.transform.scale(grass_image, (P_GRASS_WIDTH, P_GRASS_HEIGHT))
    for _ in range(P_GRASS_AMOUNT):
        x = random.randint(0, P_SCREEN_WIDTH - P_GRASS_WIDTH)
        y = random.randint(0, P_SCREEN_HEIGHT - P_GRASS_HEIGHT)
        screen.blit(grass_image, (x, y))


def draw_text(screen):
    font = pygame.font.Font(None, 20)
    title1 = font.render('Welcome to the flag game.', True, (255, 255, 255))
    title2 = font.render('Have fun!', True, (255, 255, 255))
    screen.blit(title1, (65, 15))
    screen.blit(title2, (65, 25))


#def screen_main():
pygame.init()
screen = pygame.display.set_mode((P_SCREEN_WIDTH, P_SCREEN_HEIGHT))
screen.fill(pygame.Color('green'))

draw_grass(screen)
draw_solider(screen, (0, 0))
draw_flag(screen, (P_SCREEN_WIDTH - P_FLAG_WIDTH, P_SCREEN_HEIGHT - P_FLAG_HEIGHT))
draw_text(screen)

pygame.display.flip()
