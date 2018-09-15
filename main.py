import game
import drawBoard
import time
from constants import *

def runGames(display=True, iterations=1000):
    p1Wins = 0
    p2Wins = 0
    for i in range(iterations):
        winner = runGame(display=display)
        if winner == "Player 1":
            p1Wins += 1
        else:
            p2Wins += 1
    print("Player 1 wins: " + str(p1Wins) + ", Player 2 wins: " + str(p2Wins))


def runGame(display=True):
    instance = game.Game()
    if display:
        graphics = drawBoard.DrawBoard()
        graphics.draw(instance.getBoard())
    iteration = 0
    while True:
        iteration += 1
        if DEBUG:
            print("Iteration: " + str(iteration))
        instance.processTurn()
        if (instance.winner() != None):
            return instance.winner()
        now = time.time()
        if display:
            graphics.draw(instance.getBoard())
            while (now + 1 > time.time()):
                graphics.draw(instance.getBoard())


if __name__ == "__main__":
    # winner = runGames(display=False)
    winner = runGames(display=True, iterations=1)
    if DEBUG:
        print("WINNER: " + str(winner))
