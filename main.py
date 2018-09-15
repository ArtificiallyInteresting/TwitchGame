import game
import drawBoard
import time

if __name__ == "__main__":
    instance = game.Game()
    graphics = drawBoard.DrawBoard()
    graphics.draw(instance.getBoard())
    iteration = 0
    while True:
        iteration += 1
        instance.processTurn()
        time.sleep(1)
        graphics.draw(instance.getBoard())
