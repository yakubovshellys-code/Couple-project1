import consts

def grid_init():
    game_grid = []
    for row in range(consts.ROW_GRID+1):
        game_grid.append([])
        for col in range(consts.COL_GRID+1):
            game_grid[row].append(consts.EMPTY)
    return game_grid

def soldier_init(game_grid, soldier):
    for height_body in range(soldier[0], consts.HEIGHT_BODY_SOLDIER):
        for width in range(soldier[1], consts.WIDTH_SOLDIER):
            game_grid[height_body][width] = consts.BODY_SOLDIER

    for height_legs in range(soldier[0] + consts.HEIGHT_BODY_SOLDIER, consts.HEIGHT_SOLDIER):
        for width in range(soldier[1], consts.WIDTH_SOLDIER):
            game_grid[height_legs][width] = consts.LEG_SOLDIER

def flag_init(game_grid):
    x_flag = consts.COL_GRID - consts.WIDTH_FLAG+1
    y_flag = consts.ROW_GRID - consts.HEIGHT_FLAG+1
    for row in range(y_flag, len(game_grid)):
        for col in range(x_flag, len(game_grid[row])):
            game_grid[row][col] = consts.FLAG