import pygame
import pygame_menu
from maze import Maze
from game import maze_drawer
from menu.maze_creation_menu import MazeCreationMenu


class MazeSelectorMenu:
    def __init__(self, window_size):
        self.__window_size = window_size
        self.__maze_surface = pygame.Surface((550, 550))
        self.__mazes = [
            ('Default', Maze.random_puzzle()),
            ('Black', Maze.random_puzzle()),
            ('Custom Maze', Maze.random_puzzle())
        ]
        self.__algorithms = [
            ('Default', Maze.random_puzzle()),
            ('Black', Maze.random_puzzle()),
            ('Custom Maze', Maze.random_puzzle())
        ]
        self.__maze_selector_menu = self.__factory()
        self.__cur_maze = self.mazes[0]
        self.__cur_algorithm = self.algorithms[0]

    def __change_maze(self, maze):
        maze_drawer(maze, self.__maze_surface)
        self.__cur_maze = maze

    def __change_algorithm(self, algorithm):
        self.__cur_algorithm = algorithm

    def __factory(self):
        maze_selector_menu = pygame_menu.Menu(
            height=self.__window_size[1],
            width=self.__window_size[0],
            title='Choose a maze',
            columns=2,
            rows=3,
            theme=pygame_menu.themes.THEME_DARK
        )
        maze_selector_menu.add.selector(
            title='Maze:\t',
            items=self.mazes,
            onchange=lambda _, maze: self.__change_maze(maze)
        )
        self.__algorithm = maze_selector_menu.add.dropselect(
            title='Algorithm: ',
            items=self.algorithms,
            onchange=lambda _, algorithm: self.__change_algorithm(algorithm)
        )
        maze_selector_menu.add.button('Next', self.__next_menu)
        self.__maze_surface.fill((255, 255, 255))
        maze_selector_menu.add.surface(self.__maze_surface)
        return maze_selector_menu

    @property
    def maze_selector_menu(self):
        return self.__maze_selector_menu

    @property
    def __next_menu(self) -> pygame_menu.Menu:
        return MazeCreationMenu(self.__window_size, self.__algorithm).maze_creation_menu

    @property
    def mazes(self):
        return self.__mazes

    @property
    def algorithms(self):
        return self.__algorithms
