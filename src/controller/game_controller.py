import pygame
from copy import deepcopy

import pygame_menu
from algorithms.algorithm_stats import AlgorithmStats

from view.animator import Animator, RobotAnimator
from model.sample_mazes import SAMPLE_MAZE
from view.game_view import GameView, IAView, MazeView
from model.game_model import Direction, GameModel, Maze

class Controller:

    def __init__(self, surface: pygame.Surface, game_model: GameModel):
        self._surface = surface
        self._game_model = game_model
        self._robot_animator = None

    def run(self):
        pass

    def simulate(self):
        robot_pos = self._game_model.maze.init_robot_pos
        maze = self._game_model.maze
        animator = self._robot_animator
        moves = self._game_model.moves
        robot_path = [robot_pos]
        while True:
            init_cycle_pos = deepcopy(robot_pos)
            for direction in moves:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_BACKSPACE] or keys[pygame.K_ESCAPE]:
                    print("Stop simulating")
                    return
                
                if maze.can_move(robot_pos, direction):
                    animator.move_animation(robot_pos, direction)
                    robot_pos = robot_pos.move(direction)
                    robot_path.append(robot_pos)
                else:
                    animator.cancel_animation(robot_pos, direction)
                if robot_pos == maze.final_robot_pos:
                    # Win
                    self._game_model.game_won()
                    return
                pygame.time.delay(100)
            if init_cycle_pos == robot_pos:
                # Cyclycal
                return
            pygame.time.wait(300)

    def game_win(self):
        while True:
            pygame.event.wait()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] or keys[pygame.K_BACKSPACE] or keys[pygame.K_RETURN]:
                return



class IAController(Controller):

    def __init__(self, surface: pygame.Surface, game_model: GameModel, algorithm):
        super().__init__(surface, game_model)
        self.__ia_view = IAView(surface, game_model)
        self._robot_animator: RobotAnimator = RobotAnimator(surface, self.__ia_view.maze_view, self.__ia_view)
        self.__algorithm = algorithm

    def run(self):

        results: AlgorithmStats = self.__algorithm(self._game_model)
        self._game_model.moves = results.solution_state.moves
        
        self.__ia_view.update(self._game_model)
        self.__ia_view.draw_static()
        self.__ia_view.draw_dynamic(self._game_model.maze.init_robot_pos)
        pygame.display.update()

        self.simulate()


        


class GameController(Controller):

    def __init__(self, surface: pygame.Surface, game_model: GameModel):
        super().__init__(surface, game_model)
        self.__game_view: GameView = GameView(surface, self._game_model)
        self._robot_animator: RobotAnimator = RobotAnimator(surface, self.__game_view.maze_view, self.__game_view)

    def run(self):

        running = True
        while running:
            
            self.__game_view.draw_static()
            self.__game_view.draw_dynamic(self._game_model.maze.init_robot_pos)
            
            pygame.display.update()
            pygame.event.wait()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self._game_model.add_move(Direction.UP)
            elif keys[pygame.K_DOWN]:
                self._game_model.add_move(Direction.DOWN)
            elif keys[pygame.K_LEFT]:
                self._game_model.add_move(Direction.LEFT)
            elif keys[pygame.K_RIGHT]:
                self._game_model.add_move(Direction.RIGHT)
            elif keys[pygame.K_BACKSPACE]:
                self._game_model.pop_move()
            elif keys[pygame.K_RETURN]:
                if len(self._game_model.moves) == self._game_model.no_moves:
                    self.simulate()
            elif keys[pygame.K_ESCAPE]:
                break
            else:
                continue

            self.__game_view.update(self._game_model)

            if self._game_model.victory:
                self.game_win()
                


