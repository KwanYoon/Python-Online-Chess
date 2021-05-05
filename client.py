from classes import Square
import pygame
import os
from PIL import Image

# Display setup
WIDTH = 800
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Online Chess")
FPS = 60
SQUARE_WIDTH, SQUARE_HEIGHT, SQUARE_NUM = 100, 100, 8

# Asset setup
black_king = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'black_king.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
black_queen = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'black_queen.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
black_rook = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'black_rook.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
black_bishop = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'black_bishop.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
black_knight = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'black_knight.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
black_pawn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'black_pawn.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
white_king = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'white_king.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
white_queen = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'white_queen.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
white_rook = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'white_rook.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
white_bishop = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'white_bishop.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
white_knight = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'white_knight.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))
white_pawn = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'white_pawn.png')),
                                    (SQUARE_WIDTH, SQUARE_HEIGHT))

# Colors
WHITE = (255, 255, 255)
LIGHT_BROWN = (222,184,135)
DARK_BROWN = (160,82,45)
BLACK = (0, 0, 0)

# board
board = []
for row in range(SQUARE_NUM):
    board.append([])
    for col in range(SQUARE_NUM):
        # board square
        if (row + col) % 2 == 1:
            board[row].append(Square(row, col, LIGHT_BROWN, None, None))
        else:
            board[row].append(Square(row, col, DARK_BROWN, None, None))

        # pawns
        if col == 1:
            board[row][col].image = black_pawn
            board[row][col].status = 'black'
            board[row][col].piece = 'pawn'
        elif col == 6:
            board[row][col].image = white_pawn
            board[row][col].status = 'white'
            board[row][col].piece = 'pawn'

# rooks
board[0][0].image, board[7][0].image, board[0][7].image, board[7][7].image = \
    black_rook, black_rook, white_rook, white_rook
board[0][0].status, board[7][0].status, board[0][7].status, board[7][7].status = \
    'black', 'black', 'white', 'white'
board[0][0].piece, board[7][0].piece, board[0][7].piece, board[7][7].piece = \
    'rook', 'rook', 'rook', 'rook'

# knights
board[1][0].image, board[6][0].image, board[1][7].image, board[6][7].image = \
    black_knight, black_knight, white_knight, white_knight
board[1][0].status, board[6][0].status, board[1][7].status, board[6][7].status = \
    'black', 'black', 'white', 'white'
board[1][0].piece, board[6][0].piece, board[1][7].piece, board[6][7].piece = \
    'knight', 'knight', 'knight', 'knight'

# bishops
board[2][0].image, board[5][0].image, board[2][7].image, board[5][7].image = \
    black_bishop, black_bishop, white_bishop, white_bishop
board[2][0].status, board[5][0].status, board[2][7].status, board[5][7].status = \
    'black', 'black', 'white', 'white'
board[2][0].piece, board[5][0].piece, board[2][7].piece, board[5][7].piece = \
    'bishop', 'bishop', 'bishop', 'bishop'

# king, queen
board[3][0].image, board[4][0].image, board[3][7].image, board[4][7].image = \
    black_queen, black_king, white_queen, white_king
board[3][0].status, board[4][0].status, board[3][7].status, board[4][7].status = \
    'black', 'black', 'white', 'white'
board[3][0].piece, board[4][0].piece, board[3][7].piece, board[4][7].piece = \
    'queen', 'king', 'queen', 'king'


# drawing the board
def draw_board():
    WIN.fill(WHITE)
    for row in range(SQUARE_NUM):
        for col in range(SQUARE_NUM):
            board[row][col].draw(WIN, SQUARE_WIDTH, SQUARE_HEIGHT)
    pygame.display.update()


# get grid location based on mouse location
def grid_loc():
    loc = pygame.mouse.get_pos()
    return board[loc[0] // SQUARE_WIDTH][loc[1] // SQUARE_HEIGHT]


# checking legal moves for a certain piece
def legal_moves(square):
    moves = []

    # white pieces
    if square.status == 'white':
        # pawn
        if square.piece == 'pawn':
            # if front is empty
            if not board[square.x][square.y - 1].status:
                moves.append((square.x, square.y - 1))
                if not board[square.x][square.y - 2].status and square.y == 6:
                    moves.append((square.x, square.y - 2))

            # if diagonal is possible
            if board[square.x + 1][square.y - 1].status == 'black':
                moves.append((square.x + 1, square.y - 1))
            if board[square.x - 1][square.y - 1].status == 'black':
                moves.append((square.x - 1, square.y - 1))

    # black pieces
    if square.status == 'black':
        # pawn
        if square.piece == 'pawn':
            # if front is empty
            if not board[square.x][square.y + 1].status:
                moves.append((square.x, square.y + 1))
                # if have not moved
                if not board[square.x][square.y + 2].status and square.y == 1:
                    moves.append((square.x, square.y + 2))

            # if diagonal is possible
            if board[square.x + 1][square.y + 1].status == 'white':
                moves.append((square.x + 1, square.y + 1))
            if board[square.x - 1][square.y + 1].status == 'white':
                moves.append((square.x - 1, square.y + 1))

    return moves


# main chess function
def chess():
    # updating the board
    clock = pygame.time.Clock()
    run = True
    turn = 'white'
    moving_square = None
    while run:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # moving pieces
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if first click
                if not moving_square:
                    moving_square = grid_loc()
                    # checking if turn is correct
                    if not moving_square.status or moving_square.status != turn:
                        moving_square = None

                # if second click
                else:
                    landing_square = grid_loc()
                    legal = legal_moves(moving_square)
                    print(legal)

                    # if clicked on a square with something on it
                    if landing_square.status == moving_square.status:
                        moving_square = grid_loc()
                        # checking if turn is correct
                        if not moving_square.status or moving_square.status != turn:
                            moving_square = None

                    # if different square clicked
                    elif landing_square != moving_square and (landing_square.x, landing_square.y) in legal:
                        # making a move
                        landing_square.status = moving_square.status
                        landing_square.piece = moving_square.piece
                        landing_square.image = moving_square.image
                        moving_square.status = None
                        moving_square.piece = None
                        moving_square.image = None
                        moving_square = None

                        # changing turns
                        if turn == 'white':
                            turn = 'black'
                        else:
                            turn = 'white'

        # drawing the board
        draw_board()
        clock.tick(FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chess()
