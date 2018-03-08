from board import Board
from player import PlayerMM, PlayerAB, ManualPlayer

class Game:


    def __init__(self, startBoard, player1, player2):
        self.startBoard = startBoard
        self.player1 = player1
        self.player2 = player2

    ########################################################################
    #                     Simulate a Local Game
    ########################################################################

    def simulateLocalGame(self):

        board = Board(orig=self.startBoard)
        isPlayer1 = True

        while(True):

            #finds the move to make
            if isPlayer1:
                move = self.player1.findMove(board)
            else:
                move = self.player2.findMove(board)

            #makes the move
            board.makeMove(move)
            board.print()

            #determines if the game is over or not
            isOver = board.isTerminal()
            if isOver == 0:
                print("It is a draw!")
                break
            elif isOver == 1:
                print("Player 1 wins!")
                break
            elif isOver == 2:
                print("Player 2 wins!")
                break
            else:
                isPlayer1 = not isPlayer1



if __name__ == "__main__":
    game = Game(Board(), PlayerAB(5, True), PlayerAB(5, False))
    game.simulateLocalGame()
