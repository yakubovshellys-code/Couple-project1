import pygame.key
import soldier
import consts
import game_field

def print_grid(game_grid):
    for row in range(len(game_grid)):
        print()
        for col in range(len(game_grid[row])):
            print(game_grid[row][col], end="\t")


def input_operation(game_grid):
    #if close window:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        soldier.moving(game_grid)
    #if enter

def main():
    game_grid = game_field.grid_init()
    #soldier.soldier_init(game_grid)
    game_field.flag_init(game_grid)
    mines = game_field.init_mines(game_grid)
    mines_p = game_field.row_and_col_to_pixels(mines)

    print_grid(game_grid)

    """run = True
    while run:
        input_operation()"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()