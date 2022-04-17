import pygame
from menu.main_menu import MainMenu
from maze import Maze, Position
import maze_solver.algorithms

from typing import Optional

WINDOW_SIZE = (1200, 760)

surface: Optional['pygame'] = None


def main():
    global surface

    pygame.init()
    pygame.display.set_caption('Robot Mazes')

    surface = pygame.display.set_mode(WINDOW_SIZE)

    main_menu = MainMenu(WINDOW_SIZE).main_menu

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                break

        if main_menu.is_enabled():
            main_menu.mainloop(surface)


if __name__ == '__main__':
    main()
