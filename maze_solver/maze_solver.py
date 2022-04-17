class MazeSolver:

    #algorithm_callback(Maze, N_Moves) -> RobotState
    def __init__(self):
        self.__algorithm = None
        self.__maze = None
        self.__n_moves = None

    def add_algorithm(self, algorithm_callback):
        self.__algorithm = algorithm_callback

    def add_maze(self, maze):
        self.__maze = maze

    def add_n_moves(self, n_moves):
        self.__n_moves = n_moves