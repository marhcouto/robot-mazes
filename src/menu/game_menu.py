import pygame
import pygame_menu
from view.game_view import GameView
from model.game_model import Direction



class GameMenu:
    def __init__(self, window_size, algorithm, game_model):
        self.__window_size = window_size
        self.__game_model = game_model
        self.__solution = algorithm(game_model)
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
            self.__maze_surface = pygame.Surface((550, 550))
            self.__game_view: GameView = GameView(self.__maze_surface, self.__game_model)
            self.__menu.add.label(title="Execution Time: {0}".format(self.__solution.time))
            self.__menu.add.label(title="Iterations: {0}".format(self.__solution.iterations))
            self.__menu.add.label(title="Solution Depth: {0}".format(len(self.__solution.solution_history)))
            self.__menu.add.label(title="Found Solution: {0}".format(self.__render_solution()))
            self.__menu.add.button(
                "Simulate",
                self.__animate_robot
            )
            self.__maze_surface_widget = self.__menu.add.surface(self.__maze_surface)
            self.__draw_initial_state_maze()

    def __draw_initial_state_maze(self):
        game_view = GameView(self.__maze_surface, self.__game_model)
        game_view.draw_static()
        game_view.draw_dynamic(self.__game_model.maze.init_robot_pos)

    def __animate_robot(self):
        game_view = GameView(self.__maze_surface, self.__game_model)
        cur_robot_pos = self.__game_model.maze.init_robot_pos
        solution_tuple = self.__solution.solution_history[-1::][0]

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