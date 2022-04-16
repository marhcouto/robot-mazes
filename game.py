import pygame
import pygame_menu

from maze import Maze

SQUARE_WIDTH = 50

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
                quit()

        screen.fill((255, 255, 255))
        maze_drawer(Maze.random_puzzle(), screen)
        pygame.display.flip()

        pygame.time.wait(100)
        keys = pygame.key.get_pressed()
        # print(key)





def maze_drawer(maze, screen):

    passage = EdgeFactory.no_wall()
    wall = EdgeFactory.real_wall()
    top = 50
    screen_w, _ = screen.get_size()
    left = (screen_w - maze.size * SQUARE_WIDTH) / 2
    bottom = top + maze.size * SQUARE_WIDTH
    right = left + maze.size * SQUARE_WIDTH

    # Starging house
    (initial_x, initial_y) = (maze.init_robot_pos.column * SQUARE_WIDTH + left, maze.init_robot_pos.row * SQUARE_WIDTH + top)
    pygame.draw.rect(screen, (50, 0, 150), pygame.Rect(initial_x, initial_y, SQUARE_WIDTH, SQUARE_WIDTH))

    # Starging house
    (final_x, final_y) = (maze.final_robot_pos.column * SQUARE_WIDTH + left, maze.final_robot_pos.row * SQUARE_WIDTH + top)
    pygame.draw.rect(screen, (50, 150, 150), pygame.Rect(final_x, final_y, SQUARE_WIDTH, SQUARE_WIDTH))

    # Horizontal Lines
    for i in range(maze.size):
        lines_y = i * SQUARE_WIDTH + top
        pygame.draw.line(screen, passage.color, (left, lines_y), (left + SQUARE_WIDTH * maze.size, lines_y), passage.width)

    # Vertical Lines
    for i in range(maze.size):
        line_x = i * SQUARE_WIDTH + left
        pygame.draw.line(screen, passage.color, (line_x, top), (line_x, top + SQUARE_WIDTH * maze.size), passage.width)

    # Maze frame
    pygame.draw.rect(screen, wall.color, pygame.Rect(left, top, SQUARE_WIDTH * maze.size, SQUARE_WIDTH * maze.size), wall.width)
    

    # Walls
    for position1, positions in maze.walls.items():
        for position2 in positions:
            # Horizontal wall
            if position1.column == position2.column:    
                pygame.draw.line(screen, wall.color, (position1.column * SQUARE_WIDTH + left, (maze.size - position2.row) * SQUARE_WIDTH + top), 
                    ((position1.column + 1) * SQUARE_WIDTH + left, (maze.size - position2.row) * SQUARE_WIDTH + top), wall.width)
            # Vertical wall
            else: 
                pygame.draw.line(screen, wall.color, (position2.column * SQUARE_WIDTH + left, (maze.size - position1.row) * SQUARE_WIDTH + top), 
                    (position2.column * SQUARE_WIDTH + left, (maze.size - position1.row - 1) * SQUARE_WIDTH + top), wall.width)
