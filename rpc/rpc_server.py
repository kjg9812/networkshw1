import sys
import signal
from socket import *

NUM_TRANSMISSIONS = 10
if len(sys.argv) < 2:
    print("Usage: python3 " + sys.argv[0] + " server_port")
    sys.exit(1)
assert len(sys.argv) == 2
server_port = int(sys.argv[1])

# TODO: Create a socket for the server
sock_receiver = socket(AF_INET, SOCK_DGRAM)
# Setup signal handler to exit gracefully
def cleanup(sig, frame):
    # TODO Close server's socket
    sys.exit(0)

# SIGINT is sent when you press ctrl + C, SIGTERM if you use 'kill' or leave the shell
signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)


# TODO: Bind it to server_port
sock_receiver.bind(("0.0.0.0",server_port))

# prime function
def isPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return "no"
        else:
            return "yes"
    else:
        return "no"

while True:
    # TODO: Receive RPC request from client
    data,address = sock_receiver.recvfrom(100)
    # TODO: Turn byte array that you received from client into a string variable called rpc_data
    rpc_data = data.decode()
    # TODO: Parse rpc_data to get the argument to the RPC.
    # Remember that the RPC request string is of the form prime(NUMBER)
    number = int(rpc_data[6:-1])
    # TODO: Print out the argument for debugging
    print("argument:",number)
    # TODO: Compute if the number is prime (return a 'yes' or a 'no' string)
    answer = isPrime(number)

    # TODO: Send the result of primality check back to the client who sent the RPC request
    sock_receiver.sendto(answer.encode(), address)
# TODO: Close server's socket
sock_receiver.close()