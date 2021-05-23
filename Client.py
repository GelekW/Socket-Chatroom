# Gelek Wangyal
# gmwth5
# 14273388
# 4/13/127
# This is a simple socket program written
# in Python using the Socket API

import socket
import sys
port = 13388

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), port))

# I made this function to make sure that each input has the correct
# number of arguments ie: 'login Beth Beth3 random words' would be
# invalid

def checkwordcount(string):
    word_list = string.split()
    number_of_words = len(word_list)
    return number_of_words

#msg = s.recv(1024)
#print(msg.decode("utf-8"))


#see comment over large body of commented-out code in server file
'''while 1:
    socket_list = [socket.socket(), s]
    sock_read, sock_write, error = select.select(socket_list, [], [])
    for sock in sock_read:
        # from server
        if sock == s:
            data = sock.recv(1024)
            if not data:
                sys.exit()
            else:
                x = data.decode('utf-8')
                print(str(x))
                sys.stdout.flush()
       # else:
        userInput = sys.stdin.readline()
        argument = userInput.split()[0]
        if(argument == 'newuser' and checkwordcount(userInput) == 3):
            s.send(bytes(userInput, "utf-8"))
            sys.stdout.flush()
        else:
            print("Invalid input.")
            sys.stdout.flush()
'''


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
