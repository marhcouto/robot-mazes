import pygame
import pygame_menu
from menu.maze_selector_menu import MazeSelectorMenu

from typing import Optional

from game import game

WINDOW_SIZE = (1200, 760)

surface: Optional['pygame'] = None

def choose_map():
    pass

def main_menu_factory():
    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        width=WINDOW_SIZE[0],
        title='Robot Mazes',
        theme=pygame_menu.themes.THEME_DARK
    )
    main_menu.add.button('Choose Map', MazeSelectorMenu(WINDOW_SIZE).maze_selector_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    main_menu.add.button('Play', lambda: game(surface))
    return main_menu


def main():
    global surface

    pygame.init()
    pygame.display.set_caption('Robot Mazes')

    surface = pygame.display.set_mode(WINDOW_SIZE)

    main_menu = main_menu_factory()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                break

        if main_menu.is_enabled():
            main_menu.mainloop(surface)

        print('What does this do?')


if __name__ == '__main__':
    main()
