import pygame


# squares class
class Square():
    def __init__(self, x, y, color, status, piece):
        self.x = x
        self.y = y
        self.color = color
        self.status = status
        self.piece = piece
        self.image = None

    def draw(self, win, width, height):
        pygame.draw.rect(win, self.color, (self.x * width, self.y * height, width, height))
        if self.image:
            win.blit(self.image, (self.x * width, self.y * height))
