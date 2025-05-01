
# STUDENTS - you should randomize your port number.
# This port number in practice is often a "Well Known Number"
# Students are required to document there code.
# This is sample only of a UDP server - sample only
from socket import *
serverPort = 32213
# create UDP socket and bind to your specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
# the empty string "" as the first argument means that the server socket should
#bind to all available network interfaces on the machine.
serverSocket.bind(("", serverPort))
# output to console that server is listening
print ("The Make Upper Case Server running over UDP is ready to receive ... ")
while 1:
# read client's message AND REMEMBER client's address (IP and port)
    message, clientAddress = serverSocket.recvfrom(2048)
# output to console the sentence received from client over UDP
    print ("Received from Client: ", message)
# change client's sentence to upper case letters
    modifiedMessage = message.upper()
# send back modified sentence to the client using remembered address
    serverSocket.sendto(modifiedMessage, clientAddress)
# output to console the modified sentence sent back to client
    print ("Sent back to Client: ", modifiedMessage)
