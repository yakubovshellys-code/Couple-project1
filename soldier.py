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


def if_in_grid(location):
    if location[0] < 0 or location[1] < 0:
        return False
    elif location[0] > consts.ROW_GRID - consts.SOLDIER_WIDTH or location[1] > consts.COL_GRID - consts.SOLDIER_HEIGHT:
        return False
    else:
        return True

def if_can_move(game_grid):
    x = soldier[0]
    y = soldier[1]
    for row in range(x, x + consts.SOLDIER_WIDTH):
        for col in range(y, y + consts.LEGS_SOLDIER_HEIGHT):
            if game_grid[row][col] == consts.MINE:
                return False
    return True


def remove_soldier(game_grid):
    for row in range(len(game_grid)):
        for col in range(len(game_grid[row])):
            if game_grid[row][col] == consts.SOLDIER_LEG or game_grid[row][col] == consts.SOLDIER_BODY:
                game_grid[row][col] = consts.EMPTY


def move_left(game_grid):
    new_location = (soldier[0]-1 , soldier[1])
    if if_in_grid(new_location):
        if if_can_move(game_grid):
            remove_soldier(game_grid)
            soldier_init(game_grid)
        return new_location
    return soldier

def move_right(game_grid):
    new_location = (soldier[0]+1, soldier[1])
    if if_in_grid(new_location):

        return new_location
    return soldier


def move_up(game_grid):
    new_location = (soldier[0], soldier[1]-1)
    if if_in_grid(new_location):
        return new_location
    return soldier


def move_down(game_grid):
    new_location = (soldier[0], soldier[1]+1)
    if if_in_grid(new_location):
        return new_location
    return soldier