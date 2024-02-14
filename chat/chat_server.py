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


active = True
sockets = [tcp_server]
while active:
    # Use select to see which socket is available to read from
    ready, _, _, = select.select(sockets,[],[])
    for sock in ready:
        if sock == tcp_server:
            client_socket,client_address = tcp_server.accept()
            sockets.append(client_socket)
        else:
            data = sock.recv(1024).decode()
            if data:
                print("received:",data)
                data = replace_bad_words(data).encode()
                # forward to other sockets
                for othersock in sockets:
                    if othersock != sock and othersock != tcp_server:
                        othersock.send(data)
            else:
                sock.close()
                sockets.remove(sock)



# Close sockets
for sock in sockets:
    sock.close()