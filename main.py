import time

import pygame.key
from pygame.locals import *
import soldier
import consts
import game_field
import screen

def print_grid(game_grid):
    for row in range(len(game_grid)):
        print()
        for col in range(len(game_grid[row])):
            print(game_grid[row][col], end="\t")


def won(game_grid, soldier1):
    if soldier1[0] >= consts.COL_GRID - consts.SOLDIER_WIDTH or soldier1[1] >= consts.ROW_GRID - consts.SOLDIER_HEIGHT:
        return True
    return False


def lose(game_grid, soldier1):
    for row in range(soldier1[0]+consts.BODY_SOLDIER_HEIGHT, consts.SOLDIER_HEIGHT):
        for col in range(soldier1[1], consts.SOLDIER_WIDTH):
            if game_grid[row][col] == consts.MINE:
                return True
    return False


def main():
    game_grid = game_field.grid_init()
    soldier.soldier_init(game_grid)
    game_field.flag_init(game_grid)
    mines = game_field.init_mines(game_grid)
    mines_p = game_field.row_and_col_to_pixels(mines)

    print_grid(game_grid)

    #screen.screen_main()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()

                if keys[K_LEFT]:
                    soldier.soldier = soldier.move_left(game_grid)
                elif keys[K_RIGHT]:
                    soldier.soldier = soldier.move_right(game_grid)
                elif keys[K_UP]:
                    soldier.soldier = soldier.move_up(game_grid)
                elif keys[K_DOWN]:
                    soldier.soldier = soldier.move_down(game_grid)

                print(soldier.soldier)
                new_location = game_field.row_and_col_to_pixels([soldier.soldier])
                print(new_location)

                if won(game_grid, soldier.soldier):
                    # TODO: screen winner massage
                    time.gmtime(3)
                    running = False
                elif lose(game_grid, soldier.soldier):
                    # TODO: screen loser massage
                    time.gmtime(3)
                    running = False

                screen.draw_solider(screen.screen, new_location[0])

            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()