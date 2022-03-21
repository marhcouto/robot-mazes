from enum import Enum

class Direction(Enum):
  UP = 0,
  DOWN = 1,
  LEFT = 2,
  RIGHT = 3

class Position:
  def __init__(self, row, column):
    self.__row = row
    self.__column = column

  @property
  def row(self):
    return self.__row

  @property
  def column(self):
    return self.__column

  def __str__(self) -> str:
    return "({0}, {1})".format(self.row, self.column)

  def __hash__(self) -> int:
    return (self.row, self.column).__hash__()

  def __eq__(self, __o: object) -> bool:
    return isinstance(__o, Position) and self.row == __o.row and self.column == __o.column

  def __ne__(self, __o: object) -> bool:
    return not (self == __o)

  def move(self, direction):
    match direction:
      case Direction.UP:
        return Position(self.row - 1, self.column)
      case Direction.DOWN:
        return Position(self.row + 1, self.column)
      case Direction.LEFT:
        return Position(self.row, self.column - 1)
      case Direction.RIGHT:
        return Position(self.__row, self.column + 1)

class Maze:
  def __init__(self, size, init_robot_pos, objective_pos, wall_list):
    self.__size = size
    self.__objective_pos = objective_pos
    self.__robot_pos = init_robot_pos
    self.__walls = {  }
    for wall in wall_list:
      if wall[0] in self.__walls:
        self.__walls[wall[0]].add(wall[1])
      elif wall[1] in self.__walls:
        self.__walls[wall[1]].add(wall[0])
      else:
        self.__walls[wall[0]] = set([wall[1]])

  def can_move(self, direction):
    if (not self.wall_between(self.__robot_pos, self.__robot_pos.move(direction))):
      match direction:
        case Direction.LEFT if self.__robot_pos.column > 0:
          return True
        case Direction.RIGHT if self.__robot_pos.column < (self.__size - 1):
          return True
        case Direction.UP if self.__robot_pos.row > 0:
          return True
        case Direction.DOWN if self.__robot_pos.column < (self.__size - 1):
          return True
    return False

  def move(self, direction):
    if self.can_move(direction):
      self.__robot_pos = self.__robot_pos.move(direction)
      return True
    return False
  
  def possible_moves(self):
    return [direction for direction in Direction if self.can_move(direction)]

  def wall_between(self, orig, dest):
    return (orig in self.__walls and dest in self.__walls[orig]) or (dest in self.__walls and orig in self.__walls[dest] )

  @property
  def size(self):
    return self.size

  def is_final(self):
    return self.__robot_pos == self.__objective_pos

  @property
  def robot_pos(self):
    return self.__robot_pos

maze = Maze(
  4,
  Position(1, 3),
  Position(0, 3),
  [
    (Position(2, 0), Position(2, 1)),
    (Position(1, 1), Position(1, 2)),
    (Position(0, 1), Position(0, 2)),
    (Position(0, 3), Position(1, 3)),
    (Position(1, 3), Position(2, 3))
  ]
)
