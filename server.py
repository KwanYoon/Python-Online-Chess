import socket
from _thread import *
from classes import Square
import pickle

# server settings
server = socket.gethostbyname(socket.gethostname())
port = 5555

# socket settings
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding server to socket
try:
    s.bind((server, port))
except socket.error as e:
    print(e)

# opening up port to 2 players
s.listen(2)
print("Waiting for connection, server started")
current_player = 0

# board
LIGHT_BROWN = (222, 184, 135)
DARK_BROWN = (160, 82, 45)
board = []
for row in range(8):
    board.append([])
    for col in range(8):
        # board square
        if (row + col) % 2 == 1:
            board[row].append(Square(row, col, LIGHT_BROWN, None, None))
        else:
            board[row].append(Square(row, col, DARK_BROWN, None, None))


# threaded client function
def client(conn, player):
    # continuously run when client connected
    sending = [pickle.dumps(i) for i in board]
    conn.send(sending)
    while True:
        # grab data
        try:
            # read and update player information
            data = conn.recv(2048)
            reply = [pickle.loads(i) for i in data]

            # if no data received
            if not data:
                print("Disconnected")
                break
            # if data received
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            # send to all connected
            sending = [pickle.dumps(i) for i in board]
            conn.sendall(sending)

        except:
            pass

    print("Lost connection")
    conn.close()


# Continuously look for connections (multi-threading)
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    # starting new thread for the client, and keeping track of players
    start_new_thread(client, (conn, current_player))
    current_player += 1
