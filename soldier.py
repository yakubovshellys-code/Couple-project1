import pygame

import consts

soldier = (0,0)

# Sets tha soldier (body, and legs)
def soldier_init(game_grid):
    for height_body in range(soldier[0], consts.BODY_SOLDIER_HEIGHT):
        for width in range(soldier[1], consts.SOLDIER_WIDTH):
            game_grid[height_body][width] = consts.SOLDIER_BODY

    for height_legs in range(soldier[0] + consts.BODY_SOLDIER_HEIGHT, consts.SOLDIER_HEIGHT):
        for width in range(soldier[1], consts.SOLDIER_WIDTH):
            game_grid[height_legs][width] = consts.SOLDIER_LEG


"""def if_in_grid():
    return True

def moving(keys):
    x = soldier[0]
    y = soldier[1]

    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1

    if if_in_grid():
        soldier = (x,y)"""