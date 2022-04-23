import pygame

from view.game_view import GameView, View, MazeView
from view.view_utils import SQUARE_WIDTH
from model.game_model import Maze, Position, Direction


class Animator:
    def __init__(self, surface: pygame.Surface, animated_view: View, general_view: View, frames_per_move: int = 2):
        self._animated_view = animated_view
        self._general_view = general_view
        self._surface = surface
        self._frames_per_move = frames_per_move


class RobotAnimator(Animator):
    def __init__(self, surface: pygame.Surface, animated_view: View, general_view: View, frames_per_move: int = 2):
        super().__init__(surface, animated_view, general_view, frames_per_move)

    def move_animation(self, position: Position, direction: Direction):
        current_pos: Position = self._animated_view.row_column_to_x_y(position)

        for _ in range(SQUARE_WIDTH // self._frames_per_move):
            if direction == Direction.UP:
                current_pos = (current_pos[0], current_pos[1] - self._frames_per_move)
            elif direction == Direction.DOWN:
                current_pos = (current_pos[0], current_pos[1] + self._frames_per_move)
            elif direction == Direction.LEFT:
                current_pos = (current_pos[0] - self._frames_per_move, current_pos[1])
            elif direction == Direction.RIGHT:
                current_pos = (current_pos[0] + self._frames_per_move, current_pos[1])
            self._general_view.draw_static()
            self._surface.blit(self._animated_view.robot, current_pos)
            pygame.time.delay(self._frames_per_move * 1)
            pygame.display.update()



    def cancel_animation(self, position: Position, direction: Direction):
        current_pos: Position = self._animated_view.row_column_to_x_y(position)

        for _ in range(SQUARE_WIDTH // (3 * self._frames_per_move)):
            if direction == Direction.UP:
                current_pos = (current_pos[0], current_pos[1] - self._frames_per_move)
            elif direction == Direction.DOWN:
                current_pos = (current_pos[0], current_pos[1] + self._frames_per_move)
            elif direction == Direction.LEFT:
                current_pos = (current_pos[0] - self._frames_per_move, current_pos[1])
            elif direction == Direction.RIGHT:
                current_pos = (current_pos[0] + self._frames_per_move, current_pos[1])
            self._general_view.draw_static()
            self._surface.blit(self._animated_view.robot, current_pos)
            pygame.time.delay(self._frames_per_move * 1)
            pygame.display.update()

        for _ in range(SQUARE_WIDTH // (3 * self._frames_per_move)):
            if direction == Direction.UP:
                current_pos = (current_pos[0], current_pos[1] + self._frames_per_move)
            elif direction == Direction.DOWN:
                current_pos = (current_pos[0], current_pos[1] - self._frames_per_move)
            elif direction == Direction.LEFT:
                current_pos = (current_pos[0] + self._frames_per_move, current_pos[1])
            elif direction == Direction.RIGHT:
                current_pos = (current_pos[0] - self._frames_per_move, current_pos[1])
            self._general_view.draw_static()
            self._surface.blit(self._animated_view.robot, current_pos)
            pygame.time.delay(self._frames_per_move * 1)
            pygame.display.update()

    # def movement(self, current_position: tuple, direction: Direction, duration: int):
    #     for _ in range(duration):
    #         if direction == Direction.UP:
    #             current_pos = (current_pos[0], current_pos[1] - self._frames_per_move)
    #         elif direction == Direction.DOWN:
    #             current_pos = (current_pos[0], current_pos[1] + self._frames_per_move)
    #         elif direction == Direction.LEFT:
    #             current_pos = (current_pos[0] - self._frames_per_move, current_pos[1])
    #         elif direction == Direction.RIGHT:
    #             current_pos = (current_pos[0] + self._frames_per_move, current_pos[1])
    #         self._general_view.draw_static()
    #         self._surface.blit(self._animated_view.robot, current_pos)
    #         pygame.time.delay(self._frames_per_move * 10)
    #         pygame.display.update()
