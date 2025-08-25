import consts
import grid

def print_grid(game_grid):
    for row in range(len(game_grid)):
        print()
        for col in range(len(game_grid[row])):
            print(game_grid[row][col], end="\t")

def main():
    game_grid = grid.grid_init()

    soldier = (0,0)
    grid.soldier_init(game_grid, soldier)

    print_grid(game_grid)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()