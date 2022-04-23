from tkinter import Widget
import pygame
import pygame_menu

from view.view_utils import surface
from algorithms.algorithm_stats import AlgorithmStats
from controller.game_controller import GameController
from view.animator import RobotAnimator
from view.game_view import GameView, MazeView
from model.game_model import Direction, Position, GameModel



class ComputerSolvedMazeMenu:
    def __init__(self, window_size, algorithm, game_model):
        self.__window_size = window_size
        self.__game_model: GameModel = game_model
        self.__solution: AlgorithmStats = algorithm(game_model)
        self.__menu = pygame_menu.Menu(
            height=self.__window_size[1],
            width=self.__window_size[0],
            title='I.A Play',
            columns=2,
            rows=5,
            theme=pygame_menu.themes.THEME_DARK
        )
        if not self.__solution.solution_state:
            self.__menu.add.label(title="No solution found")
        else:
            # self.__maze_surface = surface.subsurface((250, 50, 550, 550))
            self.__maze_surface = pygame.Surface((550, 550))
            self.__game_view: GameView = GameView(self.__maze_surface, self.__game_model)
            self.__menu.add.label(title="Execution Time: {0}".format(self.__solution.time))
            self.__menu.add.label(title="Iterations: {0}".format(self.__solution.iterations))
            self.__menu.add.label(title="Solution Depth: {0}".format(len(self.__solution.solution_history)))
            self.__menu.add.label(title="Found Solution: {0}".format(self.__render_solution()))
            self.__menu.add.button("Simulate", self.__animate_robot)
            self.__maze_surface_widget = self.__menu.add.surface(self.__maze_surface, selectable=True)
            self.__draw_initial_state_maze()

    def __draw_initial_state_maze(self):
        self.__game_view.draw_static()
        self.__game_view.draw_dynamic(self.__game_model.maze.init_robot_pos)

    def __animate_robot(self):
        # print(pygame.display.get_surface().get_width())
        # GameController(self.__maze_surface).run()
        self.__game_view.draw_dynamic(Position(0, 1))
        pygame.time.wait(1000)
        self.__maze_surface_widget.force_menu_surface_update()
        self.__menu.draw(surface)
        self.__game_view.draw_dynamic(Position(0, 5))
        # GameController.simulate(self.__game_model.maze, self.__solution.solution_state.moves,
        #     RobotAnimator(self.__maze_surface, self.__game_view.maze_view, self.__game_view))

    def __render_solution(self):
        res_str = "({0}".format(self.__render_direction(self.__solution.solution_history[-1::][0][0]))
        for direction in self.__solution.solution_history[-1::][0][1::]:
            res_str += ", {0}".format(self.__render_direction(direction))
        res_str += ")"
        return res_str

    @staticmethod
    def __render_direction(direction):
        if direction == Direction.UP:
            return 'U'
        elif direction == Direction.DOWN:
            return 'D'
        elif direction == Direction.LEFT:
            return 'L'
        elif direction == Direction.RIGHT:
            return 'R'

    @property
    def computer_solved_maze_menu(self):
        return self.__menu
