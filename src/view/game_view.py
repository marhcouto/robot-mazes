import pygame

from model.game_model import Maze, Position, Direction, GameModel


class View:

    def __init__(self, surface: pygame.Surface):
        self.surface = surface

    def build(self):
        pass


    def draw(self, model):
        self.build()
        pass




class MazeView(View):

    SQUARE_WIDTH = 50
    TOP = 50

    def __init__(self, surface: pygame.Surface):
        super().__init__(surface)


    def build(self, maze):
        self.__robot = self.load_robot()
        self.__left = MazeView.left(self.surface, maze)

    def left(surface: pygame.Surface, maze: Maze):
        screen_w, _ = surface.get_size()
        return (screen_w - maze.size * MazeView.SQUARE_WIDTH) / 2

    def load_robot(self):
        return pygame.transform.scale(pygame.image.load('./assets/img/robot.png'), (50, 50))
        
    def row_column_to_x_y(self, position: Position):
        return (position.column * MazeView.SQUARE_WIDTH + self.__left, position.row * MazeView.SQUARE_WIDTH + MazeView.TOP)


    def draw(self, maze: Maze):

        self.build(maze)

        passage = EdgeFactory.no_wall()
        wall = EdgeFactory.real_wall()

        # Starting house
        (initial_x, initial_y) = (maze.init_robot_pos.column * MazeView.SQUARE_WIDTH + self.__left, maze.init_robot_pos.row * MazeView.SQUARE_WIDTH + MazeView.TOP)
        pygame.draw.rect(self.surface, (50, 0, 150), pygame.Rect(initial_x, initial_y, MazeView.SQUARE_WIDTH, MazeView.SQUARE_WIDTH))

        # Ending house
        (final_x, final_y) = (maze.final_robot_pos.column * MazeView.SQUARE_WIDTH + self.__left, maze.final_robot_pos.row * MazeView.SQUARE_WIDTH + MazeView.TOP)
        pygame.draw.rect(self.surface, (50, 150, 150), pygame.Rect(final_x, final_y, MazeView.SQUARE_WIDTH, MazeView.SQUARE_WIDTH))

        # Horizontal Lines
        for i in range(maze.size):
            lines_y = i * MazeView.SQUARE_WIDTH + MazeView.TOP
            pygame.draw.line(self.surface, passage.color, (self.__left, lines_y), (self.__left + MazeView.SQUARE_WIDTH * maze.size, lines_y), passage.width)

        # Vertical Lines
        for i in range(maze.size):
            line_x = i * MazeView.SQUARE_WIDTH + self.__left
            pygame.draw.line(self.surface, passage.color, (line_x, MazeView.TOP), (line_x, MazeView.TOP + MazeView.SQUARE_WIDTH * maze.size), passage.width)

        # Maze frame
        pygame.draw.rect(self.surface, wall.color, pygame.Rect(self.__left, MazeView.TOP, MazeView.SQUARE_WIDTH * maze.size, MazeView.SQUARE_WIDTH * maze.size), wall.width)
        
        # Walls
        for position1, positions in maze.walls.items():
            for position2 in positions:
                # Horizontal wall
                if position1.column == position2.column:    
                    pygame.draw.line(self.surface, wall.color, (position1.column * MazeView.SQUARE_WIDTH + self.__left, (maze.size - position2.row) * MazeView.SQUARE_WIDTH + MazeView.TOP), 
                        ((position1.column + 1) * MazeView.SQUARE_WIDTH + self.__left, (maze.size - position2.row) * MazeView.SQUARE_WIDTH + MazeView.TOP), wall.width)
                # Vertical wall
                else: 
                    pygame.draw.line(self.surface, wall.color, (position2.column * MazeView.SQUARE_WIDTH + self.__left, (maze.size - position1.row) * MazeView.SQUARE_WIDTH + MazeView.TOP), 
                        (position2.column * MazeView.SQUARE_WIDTH + self.__left, (maze.size - position1.row - 1) * MazeView.SQUARE_WIDTH + MazeView.TOP), wall.width)
        
        # Robot
        self.surface.blit(self.__robot, (initial_x, initial_y))


    def draw_robot_moving(self, robot_from: Position, direction: Direction):
        current_pos: Position = robot_from

        for _ in range(MazeView.SQUARE_WIDTH):
            current_pos = current_pos.move(direction)
            # self.draw_robot(self, current_pos)

    def draw_robot_moving(self, position: Position):
        x, y = self.row_column_to_x_y(position)
        self.surface.blit(self.__robot, (x, y))




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




class MovesView(View):

    ARROW_WIDTH = 75

    def __init__(self, surface: pygame.Surface):
        super().__init__(surface)

    def build(self):
        self.__load_images()

    def __load_images(self):
        self.__up = pygame.transform.scale(pygame.image.load('./assets/img/arrow_up.png'), (75, 75))
        self.__down = pygame.transform.scale(pygame.image.load('./assets/img/arrow_down.png'), (75, 75))
        self.__left = pygame.transform.scale(pygame.image.load('./assets/img/arrow_left.png'), (75, 75))
        self.__right = pygame.transform.scale(pygame.image.load('./assets/img/arrow_right.png'), (75, 75))


    def draw(self, moves: list(Direction)):

        self.build()
        
        x = 10
        y = 10

        for move in moves:
            self.__draw_move(move, (x, y))
            x += self.ARROW_WIDTH

    
    def __draw_move(self, move: Direction, position: tuple):

        if move == Direction.UP:
            self.surface.blit(self.__up, position)
        elif move == Direction.DOWN:
            self.surface.blit(self.__down, position)
        elif move == Direction.LEFT:
            self.surface.blit(self.__left, position)
        elif move == Direction.RIGHT:
            self.surface.blit(self.__right, position)


class GameView(View):

    def __init__(self, surface: pygame.Surface):
        super().__init__(surface)

    def draw(self, game_model: GameModel):
        self.surface.fill((255, 255, 255))
        MazeView(self.surface).draw(game_model.maze)
        MovesView(self.surface).draw(game_model.moves)
        pygame.display.flip()