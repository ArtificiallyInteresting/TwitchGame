import pygame
from pygame.locals import *
from constants import *
import numpy
import os

class DrawBoard:
    def __init__(self, width=7, height=7):
        position = (2400,200)
        os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.imageWidth = 100
        self.imageHeight = 100
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width * self.imageWidth, height * self.imageHeight))
        pygame.display.set_caption('RPS Chess')
        self.images = {
            'R1': pygame.image.load(os.path.join('resources', 'R.png')),
            'P1': pygame.image.load(os.path.join('resources', 'P.png')),
            'S1': pygame.image.load(os.path.join('resources', 'S.png')),
            'K1': pygame.image.load(os.path.join('resources', 'K.png')),
            'R2': grayscale(pygame.image.load(os.path.join('resources', 'R.png'))),
            'P2': grayscale(pygame.image.load(os.path.join('resources', 'P.png'))),
            'S2': grayscale(pygame.image.load(os.path.join('resources', 'S.png'))),
            'K2': grayscale(pygame.image.load(os.path.join('resources', 'K.png')))
        }

    def draw(self, board):
        self.screen.fill((255,255,255))
        self.drawLines()
        images = self.getImages(board)
        for row in range(len(images)):
            for col in range(len(images[row])):
                if images[row][col] is not None:
                    self.screen.blit(images[row][col], (col*self.imageWidth, row * self.imageHeight))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()

    def drawLines(self):
        for x in range(self.width):
            pygame.draw.rect(self.screen, (0,0,0), (x * self.imageWidth, 0, 1, self.imageHeight * self.height))
        for y in range(self.height):
            pygame.draw.rect(self.screen, (0,0,0), (0, y * self.imageHeight, self.imageWidth * self.width, 1))

    def getImages(self, board):
        images = []
        for row in board:
            imagesRow = []
            for item in row:
                if item == PIECES.R1:
                    imagesRow.append(self.images['R1'])
                elif item == PIECES.P1:
                    imagesRow.append(self.images['P1'])
                elif item == PIECES.S1:
                    imagesRow.append(self.images['S1'])
                elif item == PIECES.K1:
                    imagesRow.append(self.images['K1'])
                elif item == PIECES.R2:
                    imagesRow.append(self.images['R2'])
                elif item == PIECES.P2:
                    imagesRow.append(self.images['P2'])
                elif item == PIECES.S2:
                    imagesRow.append(self.images['S2'])
                elif item == PIECES.K2:
                    imagesRow.append(self.images['K2'])
                else:
                    imagesRow.append(None)
            images.append(imagesRow)
        return images

#https://stackoverflow.com/questions/10261440/how-can-i-make-a-greyscale-copy-of-a-surface-in-pygame
def grayscale(img):
    arr = pygame.surfarray.array3d(img)
    # luminosity filter
    avgs = [[(r * 0.298 + g * 0.587 + b * 0.114) for (r, g, b) in col] for col in arr]
    arr = numpy.array([[[avg, avg, avg] for avg in col] for col in avgs])
    return pygame.surfarray.make_surface(arr)