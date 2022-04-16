import pygame

from game_model import Maze, Position, Direction, GameModel




class MazeView:

    SQUARE_WIDTH = 50


    def __init__(self, surface: pygame.Surface, maze: Maze):
        self.__maze = maze
        self.__surface = surface
        self.__robot = pygame.transform.scale(pygame.image.load('./assets/img/robot.png'), (50, 50))
        

    def draw(self):

        passage = EdgeFactory.no_wall()
        wall = EdgeFactory.real_wall()
        top = 50
        screen_w, _ = self.__surface.get_size()
        left = (screen_w - self.__maze.size * MazeView.SQUARE_WIDTH) / 2

        # Starting house
        (initial_x, initial_y) = (self.__maze.init_robot_pos.column * MazeView.SQUARE_WIDTH + left, self.__maze.init_robot_pos.row * MazeView.SQUARE_WIDTH + top)
        pygame.draw.rect(self.__surface, (50, 0, 150), pygame.Rect(initial_x, initial_y, MazeView.SQUARE_WIDTH, MazeView.SQUARE_WIDTH))

        # Ending house
        (final_x, final_y) = (self.__maze.final_robot_pos.column * MazeView.SQUARE_WIDTH + left, self.__maze.final_robot_pos.row * MazeView.SQUARE_WIDTH + top)
        pygame.draw.rect(self.__surface, (50, 150, 150), pygame.Rect(final_x, final_y, MazeView.SQUARE_WIDTH, MazeView.SQUARE_WIDTH))

        # Horizontal Lines
        for i in range(self.__maze.size):
            lines_y = i * MazeView.SQUARE_WIDTH + top
            pygame.draw.line(self.__surface, passage.color, (left, lines_y), (left + MazeView.SQUARE_WIDTH * self.__maze.size, lines_y), passage.width)

        # Vertical Lines
        for i in range(self.__maze.size):
            line_x = i * MazeView.SQUARE_WIDTH + left
            pygame.draw.line(self.__surface, passage.color, (line_x, top), (line_x, top + MazeView.SQUARE_WIDTH * self.__maze.size), passage.width)

        # Maze frame
        pygame.draw.rect(self.__surface, wall.color, pygame.Rect(left, top, MazeView.SQUARE_WIDTH * self.__maze.size, MazeView.SQUARE_WIDTH * self.__maze.size), wall.width)
        
        # Walls
        for position1, positions in self.__maze.walls.items():
            for position2 in positions:
                # Horizontal wall
                if position1.column == position2.column:    
                    pygame.draw.line(self.__surface, wall.color, (position1.column * MazeView.SQUARE_WIDTH + left, (self.__maze.size - position2.row) * MazeView.SQUARE_WIDTH + top), 
                        ((position1.column + 1) * MazeView.SQUARE_WIDTH + left, (self.__maze.size - position2.row) * MazeView.SQUARE_WIDTH + top), wall.width)
                # Vertical wall
                else: 
                    pygame.draw.line(self.__surface, wall.color, (position2.column * MazeView.SQUARE_WIDTH + left, (self.__maze.size - position1.row) * MazeView.SQUARE_WIDTH + top), 
                        (position2.column * MazeView.SQUARE_WIDTH + left, (self.__maze.size - position1.row - 1) * MazeView.SQUARE_WIDTH + top), wall.width)
        
        # Robot
        self.__surface.blit(self.__robot, (initial_x, initial_y))


    def draw_robot(self, robot_pos: Position):
        self.__surface.blit(self.__robot, (robot_pos.column, robot_pos.row))


    def draw_robot_moving(self, robot_from: Position, direction: Direction):
        current_pos: Position = robot_from

        for _ in range(MazeView.SQUARE_WIDTH):
            current_pos = current_pos.move(direction)
            self.draw_robot(self, current_pos)


    @property
    def maze(self):
        return self.__maze
    

    @property
    def surface(self):
        return self.__surface




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




class MovesView:

    def __init__(self, surface: pygame.Surface, options: list = []):
        self.__surface = surface
        self.__options = options

    def draw(self):
        pass




class GameView:

    def __init__(self, game_model: GameModel, surface: pygame.Surface):
        self.__game_model = game_model
        self.__surface = surface
        self.__maze_view = MazeView(surface, game_model.maze)
        self.__options_view = MovesView(surface)


    def draw(self):
        self.__surface.fill((255, 255, 255))
        self.__maze_view.draw()
        self.__options_view.draw()