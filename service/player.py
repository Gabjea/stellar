from abc import abstractmethod


class Player:
    def __init__(self,board):
        self.__board = board

        @abstractmethod
        def place(self,*args):
            pass
