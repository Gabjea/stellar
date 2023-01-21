from board.cell import Cell

class Board:
    def __init__(self,rows,colls):
        self.__cells = []
        self.__rows = rows
        self.__colls = colls
        self.__create_board(self.__rows,self.__colls)

    def __create_board(self,rows,cols):
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(Cell(i,j,'',False))
            self.__cells.append(row)
            

    def can_place_star(self,x,y):
        if x < 0 or y < 0 or x > 7 or y > 7:
            return False

        if self.__cells[y][x].val == '*':
            return False

        if y+1 <= 7:
            if self.__cells[y+1][x].val == '*':
                return False

        if y-1 >= 0:
            if self.__cells[y-1][x].val == '*':
                return False

        if x+1 <= 7:
            if self.__cells[y][x+1].val == '*':
                return False

        if x-1 >= 0:
            if self.__cells[y][x-1].val == '*':
                return False

        if x-1 >= 0 and y-1 >=0:
            if self.__cells[y-1][x-1].val == '*':
                return False
        
        if x+1 <= 7 and y+1 <=7:
            if self.__cells[y+1][x+1].val == '*':
                return False

        if x+1 <= 7 and y-1 >=0:
            if self.__cells[y-1][x+1].val == '*':
                return False

        if x-1 >= 0 and y+1 <=7:
            if self.__cells[y+1][x-1].val == '*':
                return False

        return True


    def can_place_ship(self,x,y):
        if x < 0 or y < 0 or x > 7 or y > 7:
            return False

        if self.__cells[y][x].val == '*' or self.__cells[y][x].val == 'E':
            return False
        
        return True

    def place(self,x,y,val):
        if val == '*':
            if self.can_place_star(x,y):
                self.__cells[y][x].val = val
                self.__cells[y][x].visible= True
                return self.__cells[y][x]

        if val == 'E':
            if self.can_place_ship(x,y):
                self.__cells[y][x].val = val
                self.__cells[y][x].visible= True
                self.__make_cruisers_visible(x,y)
                return self.__cells[y][x]
        if val == 'B':
            if self.can_place_ship(x,y):
                self.__cells[y][x].val = val
                
                return self.__cells[y][x]
        return None

    def __make_cruisers_visible(self,x,y):
        if y+1 <= 7:
            if self.__cells[y+1][x].val == 'B':
                self.__cells[y+1][x].visible = True


        if y-1 >= 0:
            if self.__cells[y-1][x].val == 'B':
                self.__cells[y-1][x].visible = True
            
        if x+1 <= 7:
            if self.__cells[y][x+1].val == 'B':
                self.__cells[y][x+1].visible = True


        if x-1 >= 0:
            if self.__cells[y][x-1].val == 'B':
                self.__cells[y][x-1].visible = True


        if x-1 >= 0 and y-1 >=0:
            if self.__cells[y-1][x-1].val == 'B':
                self.__cells[y-1][x-1].visible = True

        
        if x+1 <= 7 and y+1 <=7:
            if self.__cells[y+1][x+1].val == 'B':
                self.__cells[y+1][x+1].visible = True
            
        if x+1 <= 7 and y-1 >=0:
            if self.__cells[y-1][x+1].val == 'B':
                self.__cells[y-1][x+1].visible = True


        if x-1 >= 0 and y+1 <=7:
            if self.__cells[y+1][x-1].val == 'B':
                self.__cells[y+1][x-1].visible = True
                

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__colls

    @property
    def cells(self):
        return self.__cells


