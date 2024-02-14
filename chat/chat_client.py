import sys
import signal
import sys
import select
from socket import *
import builtins

if len(sys.argv) != 3:
    print("Usage: python3 " + sys.argv[0] + "server_address server_port")
    sys.exit(1)

# Redefine print for autograder -- do not modify
def print(*args, **kwargs):
    builtins.print(*args, **kwargs, flush=True)

server_address = sys.argv[1]
relay_port = int(sys.argv[2])

# Create a socket for the sender
tcp_client = socket(AF_INET,SOCK_STREAM)
# Connect sender to the server at the server_port
tcp_client.connect((server_address, relay_port))
# Set up a list of file descriptors to read from
stdin = sys.stdin.fileno()
all_fds = [stdin,tcp_client.fileno()] # Add your sockets fileno() here

# Repeat until server goes down or user stops entering in data
while True:
    ready_fds, _, _ = select.select(all_fds, [],[], 5)
    
    # Send data if you stdin is in ready_fds (i.e. if user pressed enter)
    if stdin in ready_fds:
        response = sys.stdin.readline().strip()
        tcp_client.send(response.encode())
    # Receive data if socket fileno is in ready_fds
    if tcp_client.fileno() in ready_fds:
        data = tcp_client.recv(1024).decode()
        if not data:
            break
        else:
            print("recieved:",data)

# Close the socket
tcp_client.close()