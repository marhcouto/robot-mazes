import pygame
import pygame_menu
import algorithms.algorithms
from menu.maze_creation_menu import MazeCreationMenu
from menu.computer_solved_maze_menu import ComputerSolvedMazeMenu
from model.sample_mazes import SAMPLE_MAZE
from view.game_view import MazeView


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
            ('Breadth-First Search', algorithms.algorithms.breadth_first_search),
            ('Depth-First Search', algorithms.algorithms.depth_first_search),
            ('Iterative Deepening DFS', algorithms.algorithms.iterative_deepening_search)
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
            maze_view = MazeView(self.__maze_surface, self.mazes[self.__cur_maze][1].maze)
            maze_view.draw_static()
            maze_view.draw_dynamic(self.mazes[self.__cur_maze][1].maze.init_robot_pos)
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
            maze_view = MazeView(self.__maze_surface, self.mazes[self.__cur_maze][1].maze)
            maze_view.draw_static()
            maze_view.draw_dynamic(self.mazes[self.__cur_maze][1].maze.init_robot_pos)
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