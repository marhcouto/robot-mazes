from src.model.game_model import Maze, GameModel, Position

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
