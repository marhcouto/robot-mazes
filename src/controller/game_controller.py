import pygame
from copy import deepcopy

from view.animator import Animator, RobotAnimator
from model.sample_mazes import SAMPLE_MAZE
from view.game_view import GameView
from model.game_model import Direction, GameModel, Maze


class GameController:

    def __init__(self, surface: pygame.Surface):
        print('Game controller constructed')
        self.__surface = surface
        self.__game_model: GameModel = SAMPLE_MAZE
        self.__game_view: GameView = GameView(surface, self.__game_model)
        self.__robot_animator: RobotAnimator = RobotAnimator(surface, self.__game_view.maze_view, self.__game_view)

    def run(self):

        print('Running game')
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            print(pygame.display.get_surface().get_width())

            # Draw
            self.__game_view.draw_static()
            self.__game_view.draw_dynamic(self.__game_model.maze.init_robot_pos)
            pygame.display.flip()
            pygame.display.update()

            pygame.event.wait()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.__game_model.add_move(Direction.UP)
            elif keys[pygame.K_DOWN]:
                self.__game_model.add_move(Direction.DOWN)
            elif keys[pygame.K_LEFT]:
                self.__game_model.add_move(Direction.LEFT)
            elif keys[pygame.K_RIGHT]:
                self.__game_model.add_move(Direction.RIGHT)
            elif keys[pygame.K_BACKSPACE]:
                self.__game_model.pop_move()
            elif keys[pygame.K_RETURN]:
                self.__game_model.simulate(self.__robot_animator, self.__game_model.moves)
            else:
                continue
            
            self.__game_view.update(self.__game_model)



    def simulate(maze: Maze, moves, animator: Animator):
        robot_pos = maze.init_robot_pos
        robot_path = [robot_pos]
        while True:
            init_cycle_pos = deepcopy(robot_pos)
            for direction in moves:
                if maze.can_move(robot_pos, direction):
                    animator.animate(robot_pos, direction)
                    if robot_pos.move(direction) == maze.final_robot_pos:
                        robot_path.append(robot_pos.move(direction))
                        return True, robot_path
                    robot_pos = robot_pos.move(direction)
                    robot_path.append(robot_pos)
            if init_cycle_pos == robot_pos:
                return False, robot_path
