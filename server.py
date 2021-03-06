import socket
import sys
import pickle
from _thread import *
from network import Network
from player import Player
from random import randint
from bullet import Bullet

server = "10.65.0.202"
port = 5555
gameID = 0
new_playerID = 0
games = {}
information_to_send = {}
#bullets = []
bullets = {}
players_on_server = {}

# Creates a socket and init the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the port to the local server
try:
    s.bind((server, port))
except socket.error as e:
    print(e)
 
# Always listens for the other connections
s.listen()
print("Waiting for connection, Server Started")

def threaded_client(conn, playerID):
    new_player = Player(playerID, 150, 150, (255,0,200), 100, 100)

    print("Sending PlayerID")
    players_on_server.update({new_player.playerID: new_player})
    conn.send(pickle.dumps(new_player))
    
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players_on_server[data["player"].playerID] = data["player"]

            for each_bullet_key,each_bullet_value in data["bullets"].items():
                if bool(each_bullet_value.exist):
                    bullets.update({each_bullet_key:each_bullet_value})
                elif not bool(each_bullet_value.exist):
                    bullets.update({each_bullet_key:each_bullet_value})
                    del bullets[each_bullet_key]

            if not data:
                print("Disconnected from the server")
                break
            else:
                information_to_send.update({'players_on_server':players_on_server})
                information_to_send.update({'bullets':bullets})
                # print("information_to_send: %s"%(information_to_send))
                conn.sendall(pickle.dumps(information_to_send))
        except:
            print("Disconnected from the server")
            try:
                del players_on_server[playerID]
            except:
                print("Name was not found")
                break
            break

    print("Connection lost")
    conn.close()

while True:
    # Always accept the connection
    conn, addr = s.accept()
    print("Connected to: ", addr)

    # After the connection was accepted, start multythreading so many connections could be established simoltaniously
    start_new_thread(threaded_client, (conn, new_playerID))
    new_playerID += 1