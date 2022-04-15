import pygame
import pygame_menu

from typing import Optional

from game import game
from maze import Maze



WINDOW_SIZE = (900, 600)

main_menu: Optional['pygame_menu.Menu'] = None
surface: Optional['pygame'] = None

def choose_map():
    pass

def main():
    global main_menu
    global surface

    pygame.init()

    surface = pygame.display.set_mode(WINDOW_SIZE)
    main_menu = pygame_menu.Menu(
        height = WINDOW_SIZE[1],
        width = WINDOW_SIZE[0],
        title = 'Robot Mazes',
        theme = pygame_menu.themes.THEME_DARK
    )

    main_menu.add.button('Choose Map', choose_map)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    main_menu.add.button('Play', lambda : game(surface))
    pygame.display.set_caption('Robot Mazes')
    
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

        pygame.display.flip()

if __name__ == '__main__':
    main()
