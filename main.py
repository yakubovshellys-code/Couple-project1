import consts

def main(name):
    game_grid = []
    for row in range(consts.ROW_GRID):
        game_grid.append([])
        for col in range(consts.COL_GRID):
            game_grid[row].append(consts.EMPTY)
    print(game_grid)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()