# Gelek Wangyal
# gmwth5
# 14273388
# 4/13/127
# This is a simple socket program written
# in Python using the Socket API

import socket
import sys
port = 13388
BUFFER = 1024

#sets up socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), port))
s.listen(5)

#global login variables
logged_in = 0
current_user = None



# newuser function parses file for matching username, returns an error message if matched
# otherwise, adds it to users.txt
def newuser(username, password):
    with open('users.txt', 'r+') as file:
        contents = file.read()
        if ('(' + username + ',') in contents:
            clientsocket.send(bytes("Denied. User account already exists.", 'utf-8'))
        else:
            file.write('\n(' + username + ', ' + password + ')')
            clientsocket.send(bytes("New user account created. Please login.", 'utf-8'))

# login function parses files for matching credentials, returns error message to client if
# not found, otherwise logs user in
def login(username, password):
    global logged_in
    global current_user
    with open('users.txt', 'r') as file:
        contents = file.read()
        if ('(' + message.split()[1] + ', ' + message.split()[2] + ')') in contents:
            logged_in = 1
            current_user = message.split()[1]
            print(logged_in)
            print(current_user)
            clientsocket.send(bytes("login confirmed", 'utf-8'))
        else:
            clientsocket.send(bytes("Denied. User name or password incorrrect", 'utf-8'))

# send function broadcasts message if logged in, otherwise returns error message
def send(message):
    global logged_in
    global current_user
    if(logged_in == 1):
        split_string = message.split(' ', 1)
        newmessage = split_string[1:][0]
        clientsocket.send(bytes(current_user + ': ' + newmessage, 'utf-8'))
    else:
        clientsocket.send(bytes("Denied. Please login first", 'utf-8'))

def logout():
    global current_user
    global logged_in
    if(logged_in == 0):
        clientsocket.send(bytes('Denied. Please login first', 'utf-8'))
    else:
        clientsocket.send(bytes(str(current_user) + ' left.', 'utf-8'))
        current_user = None
        logged_in = 0


# socket_list =  [socket.socket(), s]
# Below is a method I tried to use to get the infinite client/server loops going.
# I originally couldn't figure out why the loop was breaking after 1 to 2 messages
# So I used this method I found online to try and see if it worked, and it actually
# crashed the entire program. I later figured out because to keep the loop going, all
# I had to do was make sure that something was sent back and forth every time, and it felt
# good to figure it out on my own without an internet solution to the problem. I just wanted
# to keep it here to mark my progress with obstacles during the project though.
'''while 1:
    sock_read, sock_write, error = select.select(socket_list, [], [])

    for sock in sock_read:
        #accepts new connection from user
        if sock == s:
            clientsocket, address = s.accept()
            clientsocket.send(bytes("My chatroom client. Version One.\n", "utf-8"))

        else:
            #recieve input from user
            data = clientsocket.recvfrom(BUFFER)
            (messageData, addess) = data
            message = messageData.decode("utf-8")
            argument = message.split()[0]

            if(argument == 'newuser'):
                newuser(message.split()[1], message.split()[2])
'''
# accept client and send a success message


clientsocket, address = s.accept()
clientsocket.send(bytes("My chatroom client. Version One.\n", "utf-8"))

while True:

    print(logged_in)
    print(current_user)
    # recieve input from user
    data = clientsocket.recv(BUFFER)
    if not data:
        sys.exit()

    message = data.decode("utf-8")
    argument = message.split()[0]

    # makeshift switch case using if-else statements that runs
    # server functions based on command, no default is needed because
    # the client wouldn't send an invalid command anyways

    if(argument == 'newuser'):
        newuser(message.split()[1], message.split()[2])

    elif(argument == 'login'):
        login(message.split()[1], message.split()[2])

    elif(argument == 'send'):
        send(message)

    elif(argument == 'logout'):
        logout()

    elif(message == 'error'):
        clientsocket.send(bytes("Invalid Command", 'utf-8'))