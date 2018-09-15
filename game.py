from constants import *

class Game:
    def getBoard(self):
        return [[PIECES.PLAYER, PIECES.OPPONENT],[PIECES.OPPONENT, PIECES.PLAYER]]

    def processTurn(self):
        pass