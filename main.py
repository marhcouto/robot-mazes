from state import RobotState
from maze import Direction, Maze, Position
import algorithms

if __name__ == "__main__":
    maze = Maze(
        4,
        Position(3, 0),
        Position(0, 3),
        [
            (Position(2, 0), Position(2, 1)),
            (Position(1, 1), Position(1, 2)),
            (Position(0, 1), Position(0, 2)),
            (Position(0, 3), Position(1, 3)),
            (Position(1, 3), Position(2, 3))
        ]
    )
    print(algorithms.a_star_search(maze, 4, lambda state: 1))

