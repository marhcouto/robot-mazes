class AlgorithmStats:
    def __init__(self, time, iterations, solution_history):
        self.__time = time
        self.__iterations = iterations
        self.__solution_history = solution_history

    @property
    def time(self):
        return self.__time

    @property
    def iterations(self):
        return self.__iterations

    @property
    def solution_history(self):
        return self.__solution_history
