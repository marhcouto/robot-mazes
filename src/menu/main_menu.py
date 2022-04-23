import pygame_menu
import pygame

from menu.maze_selector_menu import MazeSelectorMenu


class MainMenu:
    def __init__(self, window_size):
        self.__main_menu = pygame_menu.Menu(
            height=window_size[1],
            width=window_size[0],
            title='Robot Mazes',
            theme=pygame_menu.themes.THEME_DARK
        )
        self.__main_menu.add.button('Choose Map', MazeSelectorMenu(window_size).maze_selector_menu)
        self.__main_menu.add.button('Quit', pygame_menu.events.EXIT)

    @property
    def main_menu(self):
        return self.__main_menu
