from constants import *

class Game:

    def getBoard(self):
        return [[PIECES.R2, PIECES.P2, PIECES.S2, PIECES.K2, PIECES.S2, PIECES.P2, PIECES.R2],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [PIECES.R1, PIECES.P1, PIECES.S1, PIECES.K1, PIECES.S1, PIECES.P1, PIECES.R1]]

    def processTurn(self):
        pass