from abc import abstractmethod
import random
from service.player import Player

class Human(Player):
    def __init__(self,board):
        super().__init__(board)
        self.__board  = board
        self.__place_ship()
    @abstractmethod
    def place(self,*args):
        x = args[0]
        y = args[1]
        val = args[2]
        
        return self.__board.place(x,y,val)

        
    def __place_ship(self):
        ship = None
        while ship is None:
            x = random.randint(0,7)
            y = random.randint(0,7)
            ship = self.place(x,y,'E')
            
