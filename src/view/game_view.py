import pygame

from model.game_model import Maze, Position, Direction, GameModel
from view.view_utils import EdgeFactory, MazeEdge


class View:

    def __init__(self, surface: pygame.Surface, model = None):
        self._surface = surface
        self._model = model
        self._build()

    def _build(self):
        pass

    def update(self, model):
        self._model = model
        self._build()

    def draw_static(self):
        pass


    def draw_dynamic(self, **data):
        pass




class MazeView(View):

    SQUARE_WIDTH = 50
    TOP = 50


    def row_column_to_x_y(self, surface: pygame.Surface, position: Position, maze: Maze):
        return (position.column * MazeView.SQUARE_WIDTH + MazeView.left(surface, maze), position.row * MazeView.SQUARE_WIDTH + MazeView.TOP)



    def left(surface: pygame.Surface, maze: Maze):
        screen_w, _ = surface.get_size()
        return (screen_w - maze.size * MazeView.SQUARE_WIDTH) / 2




    def __init__(self, surface: pygame.Surface, maze: Maze):
        super().__init__(surface, maze)


    def _build(self):
        self.__robot = MazeView.load_robot()
        self.__left = MazeView.left(self._surface, self._model)



    def load_robot():
        return pygame.transform.scale(pygame.image.load('./assets/img/robot.png'), (50, 50))
        



    def draw_static(self):

        passage: MazeEdge = EdgeFactory.no_wall()
        wall: MazeEdge = EdgeFactory.real_wall()

        # Starting house
        (initial_x, initial_y) = (self._model.init_robot_pos.column * MazeView.SQUARE_WIDTH + self.__left, self._model.init_robot_pos.row * MazeView.SQUARE_WIDTH + MazeView.TOP)
        pygame.draw.rect(self._surface, (50, 0, 150), pygame.Rect(initial_x, initial_y, MazeView.SQUARE_WIDTH, MazeView.SQUARE_WIDTH))

        # Ending house
        (final_x, final_y) = (self._model.final_robot_pos.column * MazeView.SQUARE_WIDTH + self.__left, self._model.final_robot_pos.row * MazeView.SQUARE_WIDTH + MazeView.TOP)
        pygame.draw.rect(self._surface, (50, 150, 150), pygame.Rect(final_x, final_y, MazeView.SQUARE_WIDTH, MazeView.SQUARE_WIDTH))

        # Horizontal Lines
        for i in range(self._model.size):
            lines_y = i * MazeView.SQUARE_WIDTH + MazeView.TOP
            pygame.draw.line(self._surface, passage.color, (self.__left, lines_y), (self.__left + MazeView.SQUARE_WIDTH * self._model.size, lines_y), passage.width)

        # Vertical Lines
        for i in range(self._model.size):
            line_x = i * MazeView.SQUARE_WIDTH + self.__left
            pygame.draw.line(self._surface, passage.color, (line_x, MazeView.TOP), (line_x, MazeView.TOP + MazeView.SQUARE_WIDTH * self._model.size), passage.width)

        # Maze frame
        pygame.draw.rect(self._surface, wall.color, pygame.Rect(self.__left, MazeView.TOP, MazeView.SQUARE_WIDTH * self._model.size, MazeView.SQUARE_WIDTH * self._model.size), wall.width)
        
        # Walls
        for position1, positions in self._model.walls.items():
            for position2 in positions:
                # Horizontal wall
                if position1.column == position2.column:    
                    pygame.draw.line(self._surface, wall.color, (position1.column * MazeView.SQUARE_WIDTH + self.__left, (self._model.size - position2.row) * MazeView.SQUARE_WIDTH + MazeView.TOP), 
                        ((position1.column + 1) * MazeView.SQUARE_WIDTH + self.__left, (self._model.size - position2.row) * MazeView.SQUARE_WIDTH + MazeView.TOP), wall.width)
                # Vertical wall
                else: 
                    pygame.draw.line(self._surface, wall.color, (position2.column * MazeView.SQUARE_WIDTH + self.__left, (self._model.size - position1.row) * MazeView.SQUARE_WIDTH + MazeView.TOP), 
                        (position2.column * MazeView.SQUARE_WIDTH + self.__left, (self._model.size - position1.row - 1) * MazeView.SQUARE_WIDTH + MazeView.TOP), wall.width)

        return self




    def draw_robot_moving(self, robot_from: Position, direction: Direction):
        current_pos: Position = robot_from

        for _ in range(MazeView.SQUARE_WIDTH):
            current_pos = current_pos.move(direction)
            # self.draw_robot(self, current_pos)




    def draw_dynamic(self, position: Position):
        self._surface.blit(self.__robot, self.row_column_to_x_y(self._surface, position, self._model))




# class RobotView(View):

#     def __init__(self, surface: pygame.Surface):
#         super().__init__(surface)

#     def _build(self):
#         self,__robot = self.load_robot()

#     def load_robot():
#         return pygame.transform.scale(pygame.image.load('./assets/img/robot.png'), (50, 50))
        

#     def draw(self, position: Position):
#         self.surface.blit(self.__robot, MazeView.row_column_to_x_y(position))



class MovesView(View):

    ARROW_WIDTH = 75

    def __init__(self, surface: pygame.Surface, moves: list(Direction)):
        super().__init__(surface, moves)

    def _build(self):
        self.__load_images()

    def __load_images(self):
        self.__up = pygame.transform.scale(pygame.image.load('./assets/img/arrow_up.png'), (75, 75))
        self.__down = pygame.transform.scale(pygame.image.load('./assets/img/arrow_down.png'), (75, 75))
        self.__left = pygame.transform.scale(pygame.image.load('./assets/img/arrow_left.png'), (75, 75))
        self.__right = pygame.transform.scale(pygame.image.load('./assets/img/arrow_right.png'), (75, 75))


    def draw_static(self):

        self._build()
        
        x = 10
        y = 10

        for move in self._model:
            self.__draw_move(move, (x, y))
            x += self.ARROW_WIDTH

        return self

    
    def __draw_move(self, move: Direction, position: tuple):

        if move == Direction.UP:
            self._surface.blit(self.__up, position)
        elif move == Direction.DOWN:
            self._surface.blit(self.__down, position)
        elif move == Direction.LEFT:
            self._surface.blit(self.__left, position)
        elif move == Direction.RIGHT:
            self._surface.blit(self.__right, position)




class GameView(View):

    def __init__(self, surface: pygame.Surface, model: GameModel):
        super().__init__(surface, model)
        
    
    def _build(self):
        self.__maze_view = MazeView(self._surface, self._model.maze)
        self.__moves_view = MovesView(self._surface, self._model.moves)


    def draw_static(self):
        self._surface.fill((255, 255, 255))
        self.__maze_view.draw_static()
        self.__moves_view.draw_static()


    def draw_dynamic(self, position: Position):
        self.__maze_view.draw_dynamic(position)
