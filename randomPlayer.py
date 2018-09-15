import game
import random

class RandomPlayer:
    def __init__(self):
        pass

    def getAction(self, game):
        moves = game.getPossibleMoves()
        return random.choice(moves)