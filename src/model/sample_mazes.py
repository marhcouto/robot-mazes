from model.game_model import Maze, GameModel, Position

SAMPLE_MAZE = GameModel (
    Maze(
        4,
        Position(3, 0),
        Position(0, 3),
        [
            (Position(2, 0), Position(2, 1)),
            (Position(1, 1), Position(1, 2)),
            (Position(0, 1), Position(0, 2)),
            (Position(0, 3), Position(1, 3)),
            (Position(1, 3), Position(2, 3))
        ]),
    4
)

MAZE_13 = GameModel(
    Maze(
        5,
        Position(4, 0),
        Position(0, 4),
        [
            (Position(0, 0), Position(0, 1)),
            (Position(0, 1), Position(0, 2)),
            (Position(0, 2), Position(0, 3)),
            (Position(1, 0), Position(1, 1)),
            (Position(1, 1), Position(1, 2)),
            (Position(1, 2), Position(1, 3)),
            (Position(1, 3), Position(1, 4)),
            (Position(0, 4), Position(1, 4)),
            (Position(2, 2), Position(2, 3)),
            (Position(2, 3), Position(3, 3)),
            (Position(2, 0), Position(3, 0))
        ]
    ),
    6
)
