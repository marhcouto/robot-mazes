from maze import Direction

class InvalidChangeException(Exception):
    pass


class RobotState:
    def __init__(self, tuple_of_moves, parent):
        self.tuple_of_moves = tuple_of_moves
        self.parent = parent
        self.size = len(tuple_of_moves)

    def change(self, index, direction):
        if self.tuple_of_moves[index] == direction or index < 0 or index >= self.size:
            raise InvalidChangeException
        
        return RobotState(tuple([self.tuple_of_moves[i] if i != index else direction for i in range(self.size)]), self)

    def generate_all_children(self):
        for idx in range(len(self.tuple_of_moves)):
            for direction in Direction:
                if direction != self.tuple_of_moves[idx]:
                    try:
                        yield self.change(idx, direction)
                    except InvalidChangeException:
                        print("Preconditions not met! Unexpected error!")

    def __hash__(self):
        return hash(self.tuple_of_moves)

    def __str__(self):
        return str(self.tuple_of_moves)

    def __eq__(self, other):
        return self.tuple_of_moves == other.tuple_of_moves
