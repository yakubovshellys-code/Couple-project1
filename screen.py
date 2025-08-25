
import random
import pygame
from consts import *


def draw_solider(screen, image, location):
    screen.blit(image, location)


def draw_flag(screen, image, location):
    screen.blit(image, location)


def draw_text(screen):
    font = pygame.font.Font(None, 24)
    title1 = font.render('Welcome to the flag game.', True, (255, 255, 255))
    title2 = font.render('Have fun!', True, (255, 255, 255))
    screen.blit(title1, (65, 15))
    screen.blit(title2, (65, 35))


def screen_main():
    pygame.init()
    screen = pygame.display.set_mode((P_SCREEN_WIDTH, P_SCREEN_HEIGHT))
    pygame.display.set_caption('The Flag')
    solider_image = pygame.image.load('soldier.png')
    solider_image = pygame.transform.scale(solider_image, (P_SOLIDER_WIDTH, P_SOLIDER_HEIGHT))
    flag_image = pygame.image.load('flag.png')
    flag_image = pygame.transform.scale(flag_image, (P_FLAG_WIDTH, P_FLAG_HEIGHT))
    grass_image = pygame.image.load('grass.png')
    grass_image = pygame.transform.scale(grass_image, (P_GRASS_WIDTH, P_GRASS_HEIGHT))
    grass_positions = []
    for element in range(P_GRASS_AMOUNT):
        x = random.randint(0, P_SCREEN_WIDTH - P_GRASS_WIDTH)
        y = random.randint(0, P_SCREEN_HEIGHT - P_GRASS_HEIGHT)
        grass_positions.append((x, y))
    sol_x, sol_y = 0, 0
    flag_x = P_SCREEN_WIDTH - P_FLAG_WIDTH
    flag_y = P_SCREEN_HEIGHT - P_FLAG_HEIGHT
    running = True
    while running:
        screen.fill(pygame.Color('green'))
        for pos in grass_positions:
            screen.blit(grass_image, pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            sol_x += SIZE_SQUARE
        if keys[pygame.K_LEFT]:
            sol_x -= SIZE_SQUARE
        if keys[pygame.K_UP]:
            sol_y -= SIZE_SQUARE
        if keys[pygame.K_DOWN]:
            sol_y += SIZE_SQUARE
        draw_solider(screen, solider_image, (sol_x, sol_y))
        draw_flag(screen, flag_image, (flag_x, flag_y))
        draw_text(screen)
        pygame.display.flip()
    pygame.quit()
screen_main()