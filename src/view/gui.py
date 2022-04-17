import pygame

from game_view import View


class GUI:

    def __init__(self, surface: pygame.Surface):
        self.__surface = surface


    # def update(self, game_model: GameModel):
    #     self.__surface.fill((255, 255, 255))
    #     MazeView(self.__surface, game_model.maze).draw()
    #     MovesView(self.__surface, game_model.moves).draw()
    #     pygame.display.flip()

    
    def draw(self, view: View):
        view.draw()
        pygame.display.flip()

    def draw_mul(self, views: list):
        for view in views:
            view.draw()
        self.__surface.draw
        pygame.display.flip()