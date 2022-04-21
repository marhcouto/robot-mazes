class AlgorithmStats:
    def __init__(self, time, iterations, solution_depth):
        self.__time = time
        self.__iterations = iterations
        self.__solution_depth = solution_depth

    @property
    def time(self):
        return self.__time

    @property
    def iterations(self):
        return self.__iterations

    @property
    def solution_depth(self):
        return self.__solution_depth
