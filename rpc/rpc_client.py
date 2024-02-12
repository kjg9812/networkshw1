import socket
import sys
import random

NUM_TRANSMISSIONS = 10

if len(sys.argv) > 4 or len(sys.argv) < 3:
    print("Usage: python3 " + sys.argv[0] + " server_address server_port [random_seed]")
    sys.exit(1)

if len(sys.argv) == 4:
    random_seed = int(sys.argv[3])
    random.seed(random_seed)

server_address = sys.argv[1]
server_port = int(sys.argv[2])

# TODO: Create a datagram socket for the client

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
    data = random.randint(0, 100)

    # TODO: encode this data somehow (representing the integer as a string is fine)

    # TODO: Send RPC request (i.e., rpc_data) to the server

    # TODO: Receive result back from the server into the variable result_data

    # TODO: Display it in the format "prime: yes" or "prime: no"

# TODO: Close any sockets that are open
