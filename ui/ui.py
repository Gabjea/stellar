class UI:
    def __init__(self,board,player):
        self.__board = board
        self.__player = player
    

    def print_board(self):
        cells = self.__board.cells
        rows = self.__board.rows
        cols = self.__board.cols

        print("0 1 2 3 4 5 6 7 8")
        for i in range(rows):
            print(chr(ord('A')+i),end=' ')
            for j in range(cols):
                
                if cells[i][j].visible is True:
                    print(cells[i][j].val, end = '')
                print(' ', end = '')
            print()
    

    def run_game(self):
        self.print_board()
