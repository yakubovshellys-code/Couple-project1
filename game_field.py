import random

import consts

# Initialization an empty grid
def grid_init():
    game_grid = []
    for row in range(consts.ROW_GRID+1):
        game_grid.append([])
        for col in range(consts.COL_GRID+1):
            game_grid[row].append(consts.EMPTY)
    return game_grid

# Sets the position of the flag on the grid.
def flag_init(game_grid):
    x_flag = consts.COL_GRID - consts.FLAG_WIDTH+1
    y_flag = consts.ROW_GRID - consts.FLAG_HEIGHT+1
    for row in range(y_flag, len(game_grid)):
        for col in range(x_flag, len(game_grid[row])):
            game_grid[row][col] = consts.FLAG


def random_mine():
    return (random.randint(0, consts.ROW_GRID-consts.MINE_HEIGHT), random.randint(0, consts.COL_GRID-consts.MINE_WIDTH))

def init_mines(game_grid):
    mines = []
    for i in range(consts.SUM_MINES):
        mine = random_mine()
        mines.append(mine)
        for row in range(mine[0], mine[0]+consts.MINE_HEIGHT):
            for col in range(mine[1], mine[1]+consts.MINE_WIDTH):
                game_grid[mine[0]][col] = consts.MINE
    return mines


def row_and_col_to_pixels(list):
    p_list = []
    for i in range(len(list)):
        p_list.append((list[i][0] * consts.SIZE_SQUARE , list[i][1] * consts.SIZE_SQUARE))
    return p_list