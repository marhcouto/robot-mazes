import pygame


from game_model import Maze, GameModel
from game_view import GameView




class GameContoller:

    def __init__(self, surface):
        self.__game_model = GameModel(Maze.random_puzzle(), 5)
        self.__game_view = GameView(self.__game_model, surface)


    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.__game_view.draw()
            pygame.display.flip()
            pygame.event.wait()
            keys = pygame.key.get_pressed()


        


def animation(surface, maze, starting_position, ending_position):
    pass
