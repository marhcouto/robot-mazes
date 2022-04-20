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
        self.__iterations

    @property
    def solution_depth(self):
        self.__solution_depth

    def __str__(self):
        return "Time: " + self.__time
