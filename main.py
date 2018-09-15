import game
import drawBoard
import time
from constants import *

if __name__ == "__main__":
    instance = game.Game()
    graphics = drawBoard.DrawBoard()
    graphics.draw(instance.getBoard())
    iteration = 0
    while True:
        iteration += 1
        if DEBUG:
            print("Iteration: " + str(iteration))
        instance.processTurn()
        if (instance.winner() != None):
            print("WINNER: " + str(instance.winner()))
            exit()
        now = time.time()
        graphics.draw(instance.getBoard())
        while (now + 1 > time.time()):
            graphics.draw(instance.getBoard())
