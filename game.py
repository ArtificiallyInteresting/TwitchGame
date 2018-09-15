from constants import *
from randomPlayer import *

class Game:

    def __init__(self, player1=None, player2=None):
        self.player1Turn = True
        if player1 == None:
            player1 = RandomPlayer()
        if player2 == None:
            player2 = RandomPlayer()
        self.player1 = player1
        self.player2 = player2
        self.board = self.createBoard()

    def getBoard(self):
        return self.board

    def winner(self):
        p1King = False
        p2King = False
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == PIECES.K1:
                    p1King = True
                if self.board[row][col] == PIECES.K2:
                    p2King = True
        if not p1King:
            return "Player 2"
        if not p2King:
            return "Player 1"
        return None

    def createBoard(self):
        return [[PIECES.P2, PIECES.R2, PIECES.S2, PIECES.K2, PIECES.S2, PIECES.R2, PIECES.P2],
                [None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None],
                [PIECES.P1, PIECES.R1, PIECES.S1, PIECES.K1, PIECES.S1, PIECES.R1, PIECES.P1]
                ]

    def processTurn(self):
        if self.player1Turn:
            turn = self.player1.getAction(self)
        else:
            turn = self.player2.getAction(self)

        oldPos, newPos = turn
        if DEBUG:
            print("Move from " + str(oldPos[0]) + "," + str(oldPos[1]) + " to " + str(newPos[0]) + "," + str(newPos[1]))
        self.board[newPos[0]][newPos[1]] = self.board[oldPos[0]][oldPos[1]] #TODO validate this
        self.board[oldPos[0]][oldPos[1]] = None
        self.player1Turn = not self.player1Turn

    def getPossibleMoves(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.isCurrentPlayer(self.board[row][col]):
                    moves.extend((self.getPossibleMovesForSpace(row, col)))
        return moves

    def getPossibleMovesForSpace(self, row, col):
        moves = []
        for tempRow in range(row-1, row+2):
            for tempCol in range(col-1, col+2):
                moves.append((tempRow,tempCol))
        validatedMoves = []
        for move in moves:
            if self.validateMove(move, self.board[row][col]):
                validatedMoves.append(((row,col), move))
        return validatedMoves

    def validateMove(self, move, currentSpace):
        if move[0] < 0 or move[1] < 0 or move[0] >= len(self.board) or move[1] >= len(self.board[0]):
            return False
        newSpace = self.board[move[0]][move[1]]
        if self.isCurrentPlayer(newSpace):
            return False
        if (newSpace == PIECES.K1 or newSpace == PIECES.K2):
            return True
        if (newSpace == PIECES.R1 or newSpace == PIECES.R2):
            return currentSpace == PIECES.P1 or currentSpace == PIECES.P2
        if (newSpace == PIECES.P1 or newSpace == PIECES.P2):
            return currentSpace == PIECES.S1 or currentSpace == PIECES.S2
        if (newSpace == PIECES.S1 or newSpace == PIECES.S2):
            return currentSpace == PIECES.R1 or currentSpace == PIECES.R2
        return True

    def isCurrentPlayer(self, space):
        player1Space = False
        player2Space = False
        if space in [PIECES.K1, PIECES.P1, PIECES.R1, PIECES.S1]:
            player1Space = True
        if space in [PIECES.K2, PIECES.P2, PIECES.R2, PIECES.S2]:
            player2Space = True
        if player1Space and self.player1Turn:
            return True
        if player2Space and not self.player1Turn:
            return True
        return False