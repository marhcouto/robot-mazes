import pygame
import pygame_menu

from typing import Optional

from game_controller import GameContoller
from game_model import Maze

WINDOW_SIZE = (1200, 760)

main_menu: Optional['pygame_menu.Menu'] = None
surface: Optional['pygame'] = None


def change_maze_surface(_, maze):
    #maze_drawer(maze[0], maze[1])
    pass

def choose_map():
    pass


def main():
    global main_menu
    global surface

    pygame.init()
    pygame.display.set_caption('Robot Mazes')

    surface = pygame.display.set_mode(WINDOW_SIZE)

    maze_selector_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        width=WINDOW_SIZE[0],
        title='Choose a maze',
        theme=pygame_menu.themes.THEME_DARK
    )
    maze_surface = pygame.Surface((550, 550))
    maze_surface.fill((255, 255, 255))
    maze_selector_menu.add.surface(maze_surface)
    maze_selector_menu.add.vertical_margin(25)
    items = [
        ('Default', (Maze.random_puzzle(), maze_surface)),
        ('Black', (Maze.random_puzzle(), maze_surface)),
        ('Blue', (Maze.random_puzzle(), maze_surface))
    ]
    maze_selector_menu.add.selector(
        title='Maze:\t',
        items=items,
        onchange=change_maze_surface
    )
    maze_selector_menu.add.button('Custom Maze', None)

    custom_maze_creator = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        width=WINDOW_SIZE[0],
        title='Custom Maze',
        theme=pygame_menu.themes.THEME_DARK
    )

    main_menu = pygame_menu.Menu(
        height = WINDOW_SIZE[1],
        width = WINDOW_SIZE[0],
        title = 'Robot Mazes',
        theme = pygame_menu.themes.THEME_DARK
    )
    main_menu.add.button('Choose Map', maze_selector_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    main_menu.add.button('Play', lambda: GameContoller(surface).run())
    
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
