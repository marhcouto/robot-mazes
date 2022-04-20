class MazeSolver:
    #algorithm_callback(Maze, N_Moves) -> RobotState
    def __init__(self):
        self.__algorithm = None
        self.__game_model = None

    def add_algorithm(self, algorithm_callback):
        self.__algorithm = algorithm_callback

    def add_model(self, game_model):
        self.__game_model = game_model

    def solve_maze(self):
        return self.__algorithm(self.__maze, self.__n_moves)
