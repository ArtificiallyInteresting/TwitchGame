import game
import drawBoard
import time
from constants import *
import randomPlayer
import getKills
import scoreBasedAgent

AGENTS = {
    "Random": randomPlayer.RandomPlayer,
    "ScoreBased": scoreBasedAgent.ScoreBasedAgent,
    "GetKills": getKills.GetKills
}

def runGames(display=True, iterations=1000, player1=None, player2=None):
    p1Wins = 0
    p2Wins = 0
    for i in range(iterations):
        winner = runGame(display=display, player1=player1, player2=player2)
        if winner == "Player 1":
            p1Wins += 1
        else:
            p2Wins += 1
    if DEBUG:
        print("Player 1 wins: " + str(p1Wins) + ", Player 2 wins: " + str(p2Wins))
    return p1Wins


def runGame(display=True, player1=None, player2=None):
    instance = game.Game(player1=player1, player2=player2)
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

def runMatrix(iterations=100):
    for agent1 in AGENTS.keys():
        for agent2 in AGENTS.keys():
            p1Wins = runGames(display=False, iterations=iterations, player1=AGENTS[agent1](), player2=AGENTS[agent2]())
            print(agent1 + " beat " + agent2 + " " + str(p1Wins) + " times out of " + str(iterations))




if __name__ == "__main__":
    # winner = runGames(display=False)
    # p1Wins = runGames(display=True, iterations=1, player1=scoreBasedAgent.ScoreBasedAgent())
    # if DEBUG:
    #     print("P1 WINS: " + str(p1Wins))
    runMatrix()
