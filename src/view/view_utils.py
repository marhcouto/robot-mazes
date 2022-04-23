import pygame

WINDOW_SIZE = (1200, 760)
surface = pygame.display.set_mode(WINDOW_SIZE)

SQUARE_WIDTH = 80
ARROW_WIDTH = 40
ROBOT = pygame.transform.scale(pygame.image.load('./src/assets/img/robot.png'), (SQUARE_WIDTH, SQUARE_WIDTH))
UP_ARROW = pygame.transform.scale(pygame.image.load('./src/assets/img/arrow_up.png'), (ARROW_WIDTH, ARROW_WIDTH))
DOWN_ARROW = pygame.transform.scale(pygame.image.load('./src/assets/img/arrow_down.png'), (ARROW_WIDTH, ARROW_WIDTH))
RIGHT_ARROW = pygame.transform.scale(pygame.image.load('./src/assets/img/arrow_left.png'), (ARROW_WIDTH, ARROW_WIDTH))
LEFT_ARROW = pygame.transform.scale(pygame.image.load('./src/assets/img/arrow_right.png'), (ARROW_WIDTH, ARROW_WIDTH))
BUTTON_WIDTH = 40


class MazeEdge:

    def __init__(self, width, color):
        self.__width = width
        self.__color = color

    @property
    def width(self):
        return self.__width

    @property
    def color(self):
        return self.__color


class EdgeFactory:
    @staticmethod
    def real_wall():
        return MazeEdge(4, (0, 0, 0))

    @staticmethod
    def no_wall():
        return MazeEdge(1, (100, 100, 100))
