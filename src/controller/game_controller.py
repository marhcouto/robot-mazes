import pygame
from src.view.animator import RobotAnimator


from src.view.game_view import GameView
from src.model.game_model import Direction, Maze, GameModel


class GameController:

    def __init__(self, surface: pygame.Surface):
        self.__game_model: GameModel = GameModel(Maze.random_puzzle(), 5)
        self.__game_view: GameView = GameView(surface, self.__game_model)
        self.__robot_animator: RobotAnimator = RobotAnimator(surface, self.__game_view.maze_view, self.__game_view)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # Draw
            self.__game_view.draw_static()
            self.__game_view.draw_dynamic(self.__game_model.maze.init_robot_pos)
            pygame.display.flip()

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
