# client program

import socket
import sys
port = 13388

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), port))

# make sure that each input has the correct
def checkwordcount(string):
    word_list = string.split()
    number_of_words = len(word_list)
    return number_of_words

login = False

while True:
    # recieve output from client
    data = s.recv(1024)
    x = data.decode('utf-8')
    print(str(x))

    # makeshift switch-case based on user command (first word in input) to server
    # if no valid command is sent, an error message will be sent to client and they'll
    # reply that the input is invalid
    userInput = sys.stdin.readline()
    argument = userInput.split()[0]
    if(argument == 'newuser' and checkwordcount(userInput) == 3 and len(userInput).split()[1] < 32 and message.split()[2] > 3 and message.split()[2] <9):
        s.send(bytes(userInput, "utf-8"))
    elif(argument == 'login' and checkwordcount(userInput) == 3):
        s.send(bytes(userInput, 'utf-8'))
    elif(argument == 'send'):
        s.send(bytes(userInput, 'utf-8'))
    elif(argument == 'logout'):
        s.send(bytes(userInput, 'utf-8'))
    else:
        s.send(bytes("error", 'utf-8'))
