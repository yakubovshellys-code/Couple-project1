import time

import pygame.key
from pygame.locals import *
import soldier
from consts import *
import game_field
import screen

def print_grid(game_grid):
    for row in range(len(game_grid)):
        print()
        for col in range(len(game_grid[row])):
            print(game_grid[row][col], end="\t")


def won(game_grid, soldier1):
    if soldier1[0] >= COL_GRID - SOLDIER_WIDTH or soldier1[1] >= ROW_GRID - SOLDIER_HEIGHT:
        return True
    return False


def lose(game_grid, soldier1):
    for row in range(soldier1[0]+BODY_SOLDIER_HEIGHT, SOLDIER_HEIGHT):
        for col in range(soldier1[1], SOLDIER_WIDTH):
            if game_grid[row][col] == MINE:
                return True
    return False


def main():
    game_grid = game_field.grid_init()
    soldier.soldier_init(game_grid)
    game_field.flag_init(game_grid)
    mines = game_field.init_mines(game_grid)
    mines_p = game_field.row_and_col_to_pixels(mines)

    print_grid(game_grid)

    running = True
    while running:

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                if keys[K_LEFT]:
                    soldier.soldier = soldier.move_left(game_grid)
                if keys[K_RIGHT]:
                    soldier.soldier = soldier.move_right(game_grid)
                if keys[K_UP]:
                    soldier.soldier = soldier.move_up(game_grid)
                if keys[K_DOWN]:
                    soldier.soldier = soldier.move_down(game_grid)

                print(soldier.soldier)
                new_location = game_field.row_and_col_to_pixels([soldier.soldier])
                print(new_location)

                screen.draw_solider(screen, screen.image(SOLDIER_IMAGE, (P_SOLIDER_WIDTH, P_SOLIDER_HEIGHT)), soldier.soldier)
                pygame.display.flip()

            if won(game_grid, soldier.soldier):
                # TODO: screen winner massage
                time.gmtime(3)
                running = False
            elif lose(game_grid, soldier.soldier):
                # TODO: screen loser massage
                time.gmtime(3)
                running = False

            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()