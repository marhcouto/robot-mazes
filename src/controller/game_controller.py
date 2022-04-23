import pygame
from copy import deepcopy

import pygame_menu
from algorithms.algorithm_stats import AlgorithmStats

from view.animator import Animator, RobotAnimator
from model.sample_mazes import SAMPLE_MAZE
from view.game_view import GameView, IAView, MazeView
from model.game_model import Direction, GameModel, Maze
from view.view_utils import BUTTON_WIDTH

class Controller:

    def __init__(self, surface: pygame.Surface, game_model: GameModel):
        self._surface = surface
        self._game_model = game_model
        self._robot_animator = None
        self._moves = []

    def run(self):
        pass

    def simulate(self):
        robot_pos = self._game_model.maze.init_robot_pos
        maze = self._game_model.maze
        animator = self._robot_animator
        moves = self._moves
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
        self.__ia_view = IAView(surface, (game_model, [], AlgorithmStats(0, 0, None)))
        self._robot_animator: RobotAnimator = RobotAnimator(surface, self.__ia_view.maze_view, self.__ia_view)
        self.__algorithm = algorithm

    def run(self):

        results: AlgorithmStats = self.__algorithm(self._game_model)
        self._moves = results.solution_state.moves
        
        self.__ia_view.update((self._game_model, self._moves, results))
        self.__ia_view.draw_static()
        self.__ia_view.draw_dynamic(self._game_model.maze.init_robot_pos)
        pygame.display.update()

        self.simulate()
        self.game_win()


        


class GameController(Controller):

    def __init__(self, surface: pygame.Surface, game_model: GameModel):
        super().__init__(surface, game_model)
        self.__game_view: GameView = GameView(surface, (game_model, []))
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
            if len(self._moves) > 0 and keys[pygame.K_BACKSPACE]:
                self._moves.pop()
            if keys[pygame.K_ESCAPE]:
                break
            elif len(self._moves) < self._game_model.no_moves:
                if keys[pygame.K_UP] or (pygame.mouse.get_pos()[0] > self.__game_view.buttons[0][0] and pygame.mouse.get_pos()[0] < self.__game_view.buttons[0][0] + BUTTON_WIDTH and pygame.mouse.get_pressed()[0]):
                    self._moves.append(Direction.UP)
                elif keys[pygame.K_DOWN]:
                    self._moves.append(Direction.DOWN)
                elif keys[pygame.K_LEFT]:
                    self._moves.append(Direction.LEFT)
                elif keys[pygame.K_RIGHT]:
                    self._moves.append(Direction.RIGHT)
            elif keys[pygame.K_RETURN] and len(self._moves) == self._game_model.no_moves:
                self.simulate()
            else:
                continue

            self.__game_view.update((self._game_model, self._moves))

            if self._game_model.victory:
                self.game_win()

    def game_win(self):
        self.__game_view.draw_win()
        pygame.display.update()
        super().game_win()
                


