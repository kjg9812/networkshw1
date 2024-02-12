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

# Bind the server's socket to port

# Put listener_socket in LISTEN mode

# Accept a connection first from two clients
# OR 
# implement accepting connections from multiple clients
# by including listener_socket in event handling 


active = True

while active:
    pass
    # Use select to see which socket is available to read from

    # recv on socket that is ready to read

    # Check to see if connection is closed

    # Filter and replace bad words

    # Forward to other sockets


# Close sockets