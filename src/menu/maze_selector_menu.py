import pygame
import pygame_menu
import src.algorithms.algorithms
from src.menu.maze_creation_menu import MazeCreationMenu
from src.menu.computer_solved_maze_menu import ComputerSolvedMazeMenu
from src.model.sample_mazes import SAMPLE_MAZE
from src.view.game_view import MazeView


class MazeSelectorMenu:
    def __init__(self, window_size):
        self.__window_size = window_size
        self.__maze_surface = pygame.Surface((550, 550))
        self.__maze_selector_menu = pygame_menu.Menu(
            height=self.__window_size[1],
            width=self.__window_size[0],
            title='Choose a maze',
            columns=2,
            rows=3,
            theme=pygame_menu.themes.THEME_DARK
        )
        self.__mazes = [
            ('Sample(4x4) 4', SAMPLE_MAZE),
            ('Custom Maze', None)
        ]
        self.__algorithms = [
            ('Breadth-First Search', src.algorithms.algorithms.breadth_first_search),
            ('Depth-First Search', src.algorithms.algorithms.depth_first_search),
            ('Iterative Deepening DFS', src.algorithms.algorithms.iterative_deepening_search)
        ]
        self.__cur_maze = 0
        self.__cur_algorithm = 0
        self.__widget_list = []
        self.__update_widgets()

    def __change_maze(self):
        self.__cur_maze = self.__maze_widget.get_index()
        if not self.__updating_widgets:
            self.__update_widgets()
        if self.mazes[self.__cur_maze][1]:
            MazeView(self.__maze_surface, self.mazes[self.__cur_maze][1].maze).draw_static()
        else:
            self.__maze_surface.fill((255, 255, 255))

    def __change_algorithm(self):
        self.__cur_algorithm = self.__algorithm_widget.get_index()
        if not self.__updating_widgets:
            self.__update_widgets()

    def __update_widgets(self):
        self.__updating_widgets = True
        for widget in self.__widget_list:
            self.maze_selector_menu.remove_widget(widget)
        self.__widget_list = []
        self.__maze_widget = self.maze_selector_menu.add.selector(
            title='Maze: ',
            items=self.mazes,
            onchange=lambda _, __: self.__change_maze(),
            default=self.__cur_maze
        )
        self.__algorithm_widget = self.maze_selector_menu.add.dropselect(
            title='Algorithm: ',
            items=self.algorithms,
            onchange=lambda _, __: self.__change_algorithm(),
            default=self.__cur_algorithm
        )
        if self.mazes[self.__cur_maze][0] == 'Custom Maze':
            next_menu = MazeCreationMenu(self.__window_size, self.__algorithms[self.__cur_algorithm]).maze_creation_menu
        else:
            next_menu = ComputerSolvedMazeMenu(self.__window_size, self.algorithms[self.__cur_algorithm][1], self.mazes[self.__cur_maze][1]).computer_solved_maze_menu
        self.__maze_surface.fill((255, 255, 255))
        next_button = self.maze_selector_menu.add.button('Next', next_menu)
        maze_surface = self.maze_selector_menu.add.surface(self.__maze_surface)
        self.__widget_list = [
            self.__maze_widget,
            self.__algorithm_widget,
            next_button,
            maze_surface
        ]
        if self.mazes[self.__cur_maze][1]:
            MazeView(self.__maze_surface, self.mazes[self.__cur_maze][1].maze).draw_static()
        self.__updating_widgets = False

    @property
    def maze_selector_menu(self):
        return self.__maze_selector_menu

    @property
    def mazes(self):
        return self.__mazes

    @property
    def algorithms(self):
        return self.__algorithms
