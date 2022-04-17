from game_view import GUI, View, MazeView
from utils import Observer





class RobotAnimator(Observer):


    def __init__(self, gui: GUI, id: int):
        super().__init__()
        self.__gui = gui
        self__id = id

