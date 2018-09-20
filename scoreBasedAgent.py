import game
import random
from constants import *

class ScoreBasedAgent:
    def __init__(self):
        pass

    def getAction(self, game):
        player1 = game.player1Turn
        moves = game.getPossibleMoves()
        maxScore = -99999999
        maxMoves = []
        for move in moves:
            board = game.predictTurn(move[0], move[1])
            score = self.score(board, player1)
            if score > maxScore:
                maxMoves = [move]
                maxScore = score
            elif score == maxScore:
                maxMoves.append(move)

        return random.choice(maxMoves)

    #value my pieces being closer side of board
    #value enemy pieces missing
    #kill enemy king scored highly
    def score(self, board, player1):
        total = 0
        enemyPiecePenalty = -10
        enemyKingPenalty = -1000
        for row in range(len(board)):
            for col in range(len(board[0])):
                #If I see my own piece
                if player1 and game.isPlayer1Piece(board[row][col]):
                    if player1 and board[row][col] == PIECES.K1:
                        total += row
                    else:
                        total += (len(board) - row)
                if not player1 and game.isPlayer2Piece(board[row][col]):
                    if player1 and board[row][col] == PIECES.K1:
                        total += (len(board) - row)
                    else:
                        total += row

                #If I see an enemy piece
                if not player1 and game.isPlayer1Piece(board[row][col]):
                    total += enemyPiecePenalty
                if player1 and game.isPlayer2Piece(board[row][col]):
                    total += enemyPiecePenalty

                #If I see an enemy king
                if player1 and board[row][col] == PIECES.K2:
                    total += enemyKingPenalty
                if not player1 and board[row][col] == PIECES.K1:
                    total += enemyKingPenalty
        return total




