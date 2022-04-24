import pygame_menu
import pygame

from menu.maze_selector_menu import MazeSelectorMenu
from view.view_const import SURFACE, THEME


class IntructionsMenu:
    def __init__(self, window_size):
        self.__menu = pygame_menu.Menu(
            height=window_size[1],
            width=window_size[0],
            title='Instructions',
            theme=THEME
        )
        self.__menu.add.image('./src/assets/img/description.png', scale=(1, 1))
        
    @property
    def menu(self):
        return self.__menu
