class InvalidChangeException(Exception):
    pass

from maze import Direction

class RobotState:

    possible_directions = (Direction.UP, Direction.DOWN, Direction.RIGHT, Direction.LEFT)

    def __init__(self, tuple_of_moves, parent):
        self.tuple_of_moves = tuple_of_moves
        self.parent = parent
        self.size = len(tuple_of_moves)

    def change(self, index, direction):
        if self.tuple_of_moves[index] == direction or index < 0 or index >= self.size and direction in RobotState.possible_directions:
            raise InvalidChangeException
        
        return RobotState(tuple([self.tuple_of_moves[i] if i != index else direction for i in range(self.size)]), self)

    def initial_state(size):
        moves = []
        
        for i in range(size):
            moves.apppend(Direction.UP if i % 2 == 0 else Direction.RIGHT)

        return RobotState(tuple(moves), None)

    def __hash__(self):
        return hash(self.tuple_of_moves)

    def __str__(self):
        return str(self.tuple_of_moves)

    def __eq__(self, other):
        return self.tuple_of_moves == other.tuple_of_moves

