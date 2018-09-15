import game
import random

class GetKills:
    def __init__(self):
        pass

    def getAction(self, game):
        moves = game.getPossibleMoves()
        board = game.getBoard()
        kills = []
        for move in moves:
            if game.isOpponent(board[move[1][0]][move[1][1]]):
                kills.append(move)

        if len(kills) != 0:
            return random.choice(kills)
        return random.choice(moves)