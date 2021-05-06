import pygame
import os

# image imports
SQUARE_WIDTH, SQUARE_HEIGHT = 100, 100
legal_symbol = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'legal.png')),
                                      (SQUARE_WIDTH, SQUARE_HEIGHT))

# squares class
class Square():
    def __init__(self, x, y, color, status, piece):
        self.x = x
        self.y = y
        self.color = color
        self.status = status
        self.piece = piece
        self.image = None
        self.legal = False

    def draw(self, win, width, height):
        pygame.draw.rect(win, self.color, (self.x * width, self.y * height, width, height))
        if self.image:
            win.blit(self.image, (self.x * width, self.y * height))
        if self.legal:
            win.blit(legal_symbol, (self.x * width, self.y * height))
