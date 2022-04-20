import pygame

from src.view.game_view import GameView, View, MazeView
from src.model.game_model import Maze, Position, Direction


class Animator:
    def __init__(self, surface: pygame.Surface, animated_view: View, general_view: View):
        self._animated_view = animated_view
        self._general_view = general_view
        self._surface = surface

    def animate(self):
        pass

class RobotAnimator(Animator):
    def __init__(self, surface: pygame.Surface, animated_view: View, general_view: View):
        super().__init__(surface, animated_view, general_view)

    def animate(self, position: Position, direction: Direction):
        current_pos: Position = self._animated_view.row_column_to_x_y(position)

        for _ in range(MazeView.SQUARE_WIDTH):
            if direction == Direction.UP:
                current_pos = (current_pos[0], current_pos[1] - 1)
            elif direction == Direction.DOWN:
                current_pos = (current_pos[0], current_pos[1] + 1)
            elif direction == Direction.LEFT:
                current_pos = (current_pos[0] - 1, current_pos[1])
            elif direction == Direction.RIGHT:
                current_pos = (current_pos[0] + 1, current_pos[1])
            self._general_view.draw_static()
            self._surface.blit(self._animated_view.robot, current_pos)
            pygame.display.flip()
            pygame.time.wait(10)
