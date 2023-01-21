from board.board import Board
from service.computer import Computer
from service.human import Human
from ui.ui import UI
if __name__ == '__main__':
    board = Board(8,8)
    computer = Computer(board)
    player = Human(board)
    ui = UI(board,player)
    ui.run_game()