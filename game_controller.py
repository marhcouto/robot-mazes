import pygame


from game_model import Direction, Maze, GameModel
from game_view import GameView




class GameContoller:

    def __init__(self, surface):
        self.__game_model = GameModel(Maze.random_puzzle(), 5)
        self.__game_view = GameView(surface)


    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.__game_view.draw(self.__game_model)
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
               

        


def animation(surface, maze, starting_position, ending_position):
    pass
