import pygame
from pygame.locals import *
from constants import *
import os

class DrawBoard:
    def __init__(self, width=400, height=400):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.imageWidth = 200
        self.imageHeight = 200
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Basic Pygame program')
        self.images = {
            'player': pygame.image.load(os.path.join('resources', 'player.png')),
            'opponent': pygame.image.load(os.path.join('resources', 'opponent.png'))
        }

    def draw(self, board):
        images = self.getImages(board)
        for row in range(len(images)):
            for col in range(len(images[row])):
                self.screen.blit(images[row][col], (row * self.imageWidth, col*self.imageHeight))
        pygame.display.flip()

    def getImages(self, board):
        images = []
        for row in board:
            imagesRow = []
            for item in row:
                if item == PIECES.PLAYER:
                    imagesRow.append(self.images['player'])
                elif item == PIECES.OPPONENT:
                    imagesRow.append(self.images['opponent'])
            images.append(imagesRow)
        return images