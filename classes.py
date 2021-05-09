import pygame
import os
import socket
import pickle

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


# network class
class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.board = self.connect()

    def get_board(self):
        return self.board

    def connect(self):
        try:
            # connect to addr
            self.client.connect(self.addr)
            # return what we receive and decode it
            data = self.client.recv
            return [pickle.loads(i) for i in data]
        except:
            pass

    # for sending to the server
    def send(self, board):
        try:
            # send to the address
            sending = [pickle.dumps(i) for i in board]
            self.client.send(sending)
            # return what we receive after ending
            data = self.client.recv
            return [pickle.loads(i) for i in data]
        except socket.error as e:
            print(e)
