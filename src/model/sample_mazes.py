from model.game_model import Maze, GameModel, Position

SAMPLE_LEVEL = GameModel (
    0,
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

LEVEL_1 = GameModel(
    1,
    Maze(
        5,
        Position(4, 0),
        Position(0, 4),
        [
            (Position(0, 0), Position(0, 1)),
            (Position(0, 2), Position(1, 2)),
            (Position(1, 2), Position(1, 3)),
            (Position(0, 3), Position(0, 4)),
            (Position(1, 4), Position(2, 4)),
            (Position(2, 1), Position(2, 2)),
            (Position(2, 2), Position(3, 2))
        ]
    ),
    4
)

LEVEL_2 = GameModel(
    2,
    Maze(
        5,
        Position(4, 0),
        Position(0, 4),
        [
            (Position(0, 0), Position(1, 0)),
            (Position(0, 1), Position(1, 1)),
            (Position(0, 2), Position(1, 2)),
            (Position(0, 4), Position(1, 4)),
            (Position(1, 0), Position(1, 1)),
            (Position(1, 1), Position(2, 1)),
            (Position(2, 1), Position(2, 2)),
            (Position(2, 3), Position(2, 4)),
            (Position(3, 4), Position(4, 4)),
            (Position(3, 2), Position(4, 2))
        ]
    ),
    4
)

LEVEL_3 = GameModel(
    3,
    Maze(
        5,
        Position(4, 0),
        Position(0, 4),
        [
            (Position(0, 3), Position(0, 4)),
            (Position(1, 1), Position(1, 2)),
            (Position(1, 2), Position(2, 2)),
            (Position(2, 2), Position(3, 2)),
            (Position(2, 2), Position(2, 3)),
            (Position(2, 2), Position(3, 2)),
            (Position(3, 2), Position(3, 3)),
            (Position(3, 2), Position(4, 2)),
            (Position(4, 0), Position(4, 1))
        ]
    ),
    5
)

LEVEL_4 = GameModel(
    4,
    Maze(
        5,
        Position(4, 0),
        Position(0, 4),
        [
            (Position(0, 0), Position(0, 1)),
            (Position(0, 1), Position(1, 1)),
            (Position(0, 3), Position(1, 3)),
            (Position(0, 4), Position(1, 4)),
            (Position(1, 1), Position(1, 2)),
            (Position(1, 2), Position(2, 2)),
            (Position(2, 1), Position(3, 1)),
            (Position(2, 3), Position(2, 4)),
            (Position(2, 4), Position(3, 4))
        ]
    ),
    5
)

LEVEL_5 = GameModel(
    5,
    Maze(
        5,
        Position(4, 0),
        Position(0, 4),
        [
            (Position(0, 0), Position(0, 1)),
            (Position(0, 3), Position(0, 4)),
            (Position(1, 3), Position(2, 3)),
            (Position(2, 4), Position(3, 4)),
            (Position(1, 1), Position(2, 1)),
            (Position(2, 0), Position(2, 1)),
            (Position(2, 1), Position(2, 2)),
            (Position(3, 1), Position(3, 2)),
            (Position(4, 1), Position(4, 2))
        ]
    ),
    5
)


LEVEL_13 = GameModel(
    13,
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

IMPOSSIBLE_LEVEL = GameModel(
    Maze(
        5,
        Position(4, 0),
        Position(0, 4),
        [
            (Position(0, 0), Position(0, 1)),
            (Position(0, 1), Position(1, 1)),
            (Position(0, 1), Position(0, 2)),
            (Position(0, 3), Position(0, 4)),
            (Position(3, 3), Position(3, 4)),
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