import sys
import select
from socket import *

import builtins

# Redefine print for autograder -- do not modify
def print(*args, **kwargs):
    builtins.print(*args, **kwargs, flush=True)

bad_words = ["virus", "worm", "malware"]
good_words = ["groot", "hulk", "ironman"]

def replace_bad_words(s):
    for j in range(3):
        s = s.replace(bad_words[j], good_words[j])
    return s

if len(sys.argv) != 2:
    print("Usage: python3 " + sys.argv[0] + " port")
    sys.exit(1)
port = int(sys.argv[1])

# Create a TCP socket to listen on port for new connections
tcp_server = socket(AF_INET,SOCK_STREAM)
# Bind the server's socket to port
tcp_server.bind(('0.0.0.0',port))
# Put listener_socket in LISTEN mode
tcp_server.listen()
# Accept a connection first from two clients
# OR 
# implement accepting connections from multiple clients
# by including listener_socket in event handling 


sockets = [tcp_server]
while True:
    # Use select to see which socket is available to read from
    ready, _, _, = select.select(sockets,[],[])
    for sock in ready:
        # data in tcp_server -> accepting multiple clients
        if sock == tcp_server:
            client_socket,client_address = tcp_server.accept()
            sockets.append(client_socket)
        # data from other sockets -> filter and send to others
        else:
            data = sock.recv(100).decode()
            if data:
                print("echo received:",data)
                # replace bad words
                data = replace_bad_words(data).encode()
                # forward to all other sockets, i included the echo to the sender as well
                for othersock in sockets:
                    if othersock != tcp_server:
                        othersock.send(data)
            # if there's no data then we should close this socket
            else:
                sock.close()
                sockets.remove(sock)
