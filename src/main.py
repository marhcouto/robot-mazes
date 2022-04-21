import pygame
from menu.main_menu import MainMenu
from controller.game_controller import GameController
from typing import Optional
from algorithms.heuristic import shortest_path_heuristic
from model.sample_mazes import SAMPLE_MAZE

WINDOW_SIZE = (1200, 760)

surface: Optional['pygame'] = None


def main():
    global surface

    pygame.init()
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
    #main()
    shortest_path_heuristic(SAMPLE_MAZE, None)