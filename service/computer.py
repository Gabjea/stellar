from abc import abstractmethod
import random
from service.player import Player

class Computer(Player):
    def __init__(self,board):
        super().__init__(board)
        self.__board = board
        self.init_stars()
        self.init_cruisers()
    @abstractmethod
    def place(self,*args):
        x = args[0]
        y = args[1]
        val = args[2]
        
        return self.__board.place(x,y,val)

        
    def init_stars(self):
        stars_nr = 0
        while stars_nr != 10:
            x = random.randint(0,7)
            y = random.randint(0,7)
            place = self.place(x,y,'*')
            if place is not None:
                stars_nr += 1
    
    def init_cruisers(self):
        stars_nr = 0
        while stars_nr != 3:
            x = random.randint(0,7)
            y = random.randint(0,7)
            place = self.place(x,y,'B')
            if place is not None:
                stars_nr += 1
