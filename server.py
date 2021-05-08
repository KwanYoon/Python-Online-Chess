import socket
from _thread import *

# server settings
server = "192.168.2.197"
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
board = []


# threaded client function
def client(conn, player):
    # continuously run when client connected
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        # grab data
        try:
            # read and update player information
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            # if no data received
            if not data:
                print("Disconnected")
                break
            # if data received
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            # send to all connected
            conn.sendall(str.encode(reply))

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
