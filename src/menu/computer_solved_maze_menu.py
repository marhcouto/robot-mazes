import pygame
import pygame_menu
from view.game_view import GameView
from view.animator import RobotAnimator


class ComputerSolvedMazeMenu:
    def __init__(self, window_size, algorithm, game_model):
        self.__window_size = window_size
        self.__game_model = game_model
        self.__solution = algorithm(game_model)
        self.__menu = pygame_menu.Menu(
            height=self.__window_size[1],
            width=self.__window_size[0],
            title='I.A Play',
            columns=2,
            rows=4,
            theme=pygame_menu.themes.THEME_DARK
        )
        self.__maze_surface = pygame.Surface((550, 550))
        self.__menu.add.label(title="Execution Time: {0}".format(self.__solution.time))
        self.__menu.add.label(title="Iterations: {0}".format(self.__solution.iterations))
        self.__menu.add.label(title="Solution Depth: {0}".format(self.__solution.solution_depth))
        self.__menu.add.button(
            "Simulate",
            self.__animate_robot
        )
        self.__menu.add.surface(self.__maze_surface)
        self.__draw_initial_state_maze()

    def __draw_initial_state_maze(self):
        game_view = GameView(self.__maze_surface, self.__game_model)
        game_view.draw_static()
        game_view.draw_dynamic(self.__game_model.maze.init_robot_pos)

    def __animate_robot(self):
        game_view = GameView(self.__maze_surface, self.__game_model)
        RobotAnimator(self.__maze_surface, game_view, game_view.maze_view)

    @property
    def computer_solved_maze_menu(self):
        return self.__menu
