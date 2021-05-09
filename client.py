from classes import Square
from classes import Network
import pygame
import os

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
LIGHT_BROWN = (222, 184, 135)
DARK_BROWN = (160, 82, 45)
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


# creating string format move with given integer inputs
def make_str_move(move_x, move_y, land_x, land_y):
    return str(move_x) + "," + str(move_y) + "," + str(land_x) + "," + str(land_y)


# creating integer format move with given string input
def make_int_move(move_str):
    move_str = move_str.split(",")
    return int(move_str[0]), int(move_str[1]), int(move_str[2]), int(move_str[3])


# rook / queen moves
def rook_moves(square, opposite_color, moves):
    if square.piece == 'rook' or square.piece == 'queen':
        # right
        for i in range(square.x + 1, 7):
            if not board[i][square.y].status:
                moves.append(board[i][square.y])
            else:
                if board[i][square.y].status == opposite_color:
                    moves.append(board[i][square.y])
                break

        # left
        for i in range(square.x - 1, -1, -1):
            if not board[i][square.y].status:
                moves.append(board[i][square.y])
            else:
                if board[i][square.y].status == opposite_color:
                    moves.append(board[i][square.y])
                break

        # up
        for i in range(square.y - 1, -1, -1):
            if not board[square.x][i].status:
                moves.append(board[square.x][i])
            else:
                if board[square.x][i].status == opposite_color:
                    moves.append(board[square.x][i])
                break

        # down
        for i in range(square.y + 1, 7):
            if not board[square.x][i].status:
                moves.append(board[square.x][i])
            else:
                if board[square.x][i].status == opposite_color:
                    moves.append(board[square.x][i])
                break


# knight moves
def knight_moves(square, color, moves):
    if square.piece == 'knight':
        # top right
        if square.x + 1 <= 7 and square.y - 2 >= 0 and not board[square.x + 1][square.y - 2].status == color:
            moves.append(board[square.x + 1][square.y - 2])

        # right top
        if square.x + 2 <= 7 and square.y - 1 >= 0 and not board[square.x + 2][square.y - 1].status == color:
            moves.append(board[square.x + 2][square.y - 1])

        # right bottom
        if square.x + 2 <= 7 and square.y + 1 <= 7 and not board[square.x + 2][square.y + 1].status == color:
            moves.append(board[square.x + 2][square.y + 1])

        # bottom right
        if square.x + 1 <= 7 and square.y + 2 <= 7 and not board[square.x + 1][square.y + 2].status == color:
            moves.append(board[square.x + 1][square.y + 2])

        # bottom left
        if square.x - 1 >= 0 and square.y + 2 <= 7 and not board[square.x - 1][square.y + 2].status == color:
            moves.append(board[square.x - 1][square.y + 2])

        # left bottom
        if square.x - 2 >= 0 and square.y + 1 <= 7 and not board[square.x - 2][square.y + 1].status == color:
            moves.append(board[square.x - 2][square.y + 1])

        # left top
        if square.x - 2 >= 0 and square.y - 1 >= 0 and not board[square.x - 2][square.y - 1].status == color:
            moves.append(board[square.x - 2][square.y - 1])

        # top left
        if square.x - 1 >= 0 and square.y - 2 >= 0 and not board[square.x - 1][square.y - 2].status == color:
            moves.append(board[square.x - 1][square.y - 2])


# bishop / queen moves
def bishop_moves(square, opposite_color, moves):
    if square.piece == 'bishop' or square.piece == 'queen':
        # top right
        i = 1
        while square.x + i < 8 and square.y - i >= 0:
            loc = board[square.x + i][square.y - i]
            if loc.status:
                if loc.status == opposite_color:
                    moves.append(loc)
                break
            moves.append(loc)
            i += 1

        # bottom right
        i = 1
        while square.x + i < 8 and square.y + i < 8:
            loc = board[square.x + i][square.y + i]
            if loc.status:
                if loc.status == opposite_color:
                    moves.append(loc)
                break
            moves.append(loc)
            i += 1

        # bottom left
        i = 1
        while square.x - i >= 0 and square.y + i < 8:
            loc = board[square.x - i][square.y + i]
            if loc.status:
                if loc.status == opposite_color:
                    moves.append(loc)
                break
            moves.append(loc)
            i += 1

        # top left
        i = 1
        while square.x - i >= 0 and square.y - i >= 0:
            loc = board[square.x - i][square.y - i]
            if loc.status:
                if loc.status == opposite_color:
                    moves.append(loc)
                break
            moves.append(loc)
            i += 1


# king moves
def king_moves(square, color, moves):
    if square.piece == 'king':
        # up
        if square.y - 1 >= 0:
            # direct
            if board[square.x][square.y - 1].status != color:
                moves.append(board[square.x][square.y - 1])

            # left
            if square.x - 1 >= 0 and board[square.x - 1][square.y - 1].status != color:
                moves.append(board[square.x - 1][square.y - 1])

            # right
            if square.x + 1 < 8 and board[square.x + 1][square.y - 1].status != color:
                moves.append(board[square.x + 1][square.y - 1])

        # left
        if square.x - 1 >= 0 and board[square.x - 1][square.y].status != color:
            moves.append(board[square.x - 1][square.y])

        # right
        if square.x + 1 < 8 and board[square.x + 1][square.y].status != color:
            moves.append(board[square.x + 1][square.y])

        # down
        if square.y + 1 < 8:
            # direct
            if board[square.x][square.y + 1].status != color:
                moves.append(board[square.x][square.y + 1])

            # left
            if square.x - 1 >= 0 and board[square.x - 1][square.y + 1].status != color:
                moves.append(board[square.x - 1][square.y + 1])

            # right
            if square.x + 1 < 8 and board[square.x + 1][square.y + 1].status != color:
                moves.append(board[square.x + 1][square.y + 1])


# checking legal moves for a certain piece
def legal_moves(square):
    moves = []

    # white pieces
    if square.status == 'white':
        # pawn
        if square.piece == 'pawn':
            # if front is empty
            if not board[square.x][square.y - 1].status:
                moves.append(board[square.x][square.y - 1])
                if not board[square.x][square.y - 2].status and square.y == 6:
                    moves.append(board[square.x][square.y - 2])

            # if diagonal is possible
            if square.x < 7 and board[square.x + 1][square.y - 1].status == 'black':
                moves.append(board[square.x + 1][square.y - 1])
            if square.x > 0 and board[square.x - 1][square.y - 1].status == 'black':
                moves.append(board[square.x - 1][square.y - 1])

        # rook / queen
        rook_moves(square, 'black', moves)

        # knight
        knight_moves(square, 'white', moves)

        # bishop / queen
        bishop_moves(square, 'black', moves)

        # king
        king_moves(square, 'white', moves)

    # black pieces
    if square.status == 'black':
        # pawn
        if square.piece == 'pawn':
            # if front is empty
            if not board[square.x][square.y + 1].status:
                moves.append(board[square.x][square.y + 1])
                # if have not moved
                if not board[square.x][square.y + 2].status and square.y == 1:
                    moves.append(board[square.x][square.y + 2])

            # if diagonal is possible
            if square.x < 7 and board[square.x + 1][square.y + 1].status == 'white':
                moves.append(board[square.x + 1][square.y + 1])
            if square.x > 0 and board[square.x - 1][square.y + 1].status == 'white':
                moves.append(board[square.x - 1][square.y + 1])

        # rook
        rook_moves(square, 'white', moves)

        # knight
        knight_moves(square, 'black', moves)

        # bishop
        bishop_moves(square, 'white', moves)

        # king
        king_moves(square, 'black', moves)

    return moves


# main chess function
def chess():
    # networking
    n = Network()

    # updating the board
    clock = pygame.time.Clock()
    run = True
    turn = 'white'
    moving_square = None
    legal = []
    while run:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # moving pieces
            if event.type == pygame.MOUSEBUTTONDOWN:
                # grab square that was clicked
                clicked_square = grid_loc()

                # if there are legal moves saved, remove them
                if len(legal) != 0:
                    # if clicked square is in legal
                    if clicked_square in legal and moving_square:
                        # make move
                        clicked_square.status = moving_square.status
                        clicked_square.piece = moving_square.piece
                        clicked_square.image = moving_square.image
                        moving_square.status = None
                        moving_square.piece = None
                        moving_square.image = None
                        moving_square = None

                        # changing turns
                        if turn == 'white':
                            turn = 'black'
                        else:
                            turn = 'white'

                    # clear legal
                    for square in legal:
                        square.legal = False

                # grab legal moves and redraw the board accordingly
                if clicked_square.status == turn:
                    moving_square = clicked_square
                    legal = legal_moves(clicked_square)
                    for square in legal:
                        square.legal = True

        # send, grab, updating player 2 moves

        # drawing the board
        draw_board()
        clock.tick(FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chess()
