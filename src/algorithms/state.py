from model.game_model import Direction

class InvalidChangeException(Exception):
    pass

class RobotState:
    possible_directions = (Direction.UP, Direction.DOWN, Direction.RIGHT, Direction.LEFT)

    def __init__(self, tuple_of_moves, parent):
        self.__tuple_of_moves = tuple_of_moves
        self.__parent = parent
        self.__size = len(tuple_of_moves)

    @property
    def moves(self):
        return self.__tuple_of_moves

    @property
    def parent(self):
        return self.__parent

    def change(self, index, direction):
        if self.__tuple_of_moves[index] == direction or index < 0 or index >= self.__size and direction in RobotState.possible_directions:
            raise InvalidChangeException
        
        return RobotState(tuple([self.__tuple_of_moves[i] if i != index else direction for i in range(self.__size)]), self)

    def initial_state(size):
        moves = []
        
        for i in range(size):
            moves.append(Direction.UP if i % 2 == 0 else Direction.RIGHT)

        return RobotState(tuple(moves), None)

    def generate_all_children(self):
        for idx in range(len(self.__tuple_of_moves)):
            for direction in Direction:
                if direction != self.__tuple_of_moves[idx]:
                    try:
                        yield self.change(idx, direction)
                    except InvalidChangeException:
                        print("Preconditions not met! Unexpected error!")

    def __hash__(self):
        return hash(self.__tuple_of_moves)

    def __str__(self):
        return str(self.__tuple_of_moves)

    def __eq__(self, other):
        return self.__tuple_of_moves == other.__tuple_of_moves
