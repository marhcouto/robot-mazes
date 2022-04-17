import pygame
import pygame_menu

from maze import Maze

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
    def real_wall():
        return MazeEdge(4, (0, 0, 0))

    def no_wall():
        return MazeEdge(1, (100, 100, 100))




def game(screen):
    # Run until the user asks to quit
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        maze_drawer(Maze.random_puzzle(), screen)
        pygame.display.flip()

        pygame.time.wait(100)


def maze_drawer(maze, screen):
    square_width = 50
    passage = EdgeFactory.no_wall()
    wall = EdgeFactory.real_wall()
    top = 50
    screen_w, _ = screen.get_size()
    left = (screen_w - maze.size * square_width) / 2
    bottom = top + maze.size * square_width
    right = left + maze.size * square_width

    # Starging house
    (initial_x, initial_y) = (maze.init_robot_pos.column * square_width + left, maze.init_robot_pos.row * square_width + top)
    pygame.draw.rect(screen, (50, 0, 150), pygame.Rect(initial_x, initial_y, square_width, square_width))

    # Starging house
    (final_x, final_y) = (maze.final_robot_pos.column * square_width + left, maze.final_robot_pos.row * square_width + top)
    pygame.draw.rect(screen, (50, 150, 150), pygame.Rect(final_x, final_y, square_width, square_width))

    # Horizontal Lines
    for i in range(maze.size):
        lines_y = i * square_width + top
        pygame.draw.line(screen, passage.color, (left, lines_y), (left + square_width * maze.size, lines_y), passage.width)

    # Vertical Lines
    for i in range(maze.size):
        line_x = i * square_width + left
        pygame.draw.line(screen, passage.color, (line_x, top), (line_x, top + square_width * maze.size), passage.width)

    # Maze frame
    pygame.draw.rect(screen, wall.color, pygame.Rect(left, top, square_width * maze.size, square_width * maze.size), wall.width)
    

    # Walls
