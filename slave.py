import os
import socket
s = socket.socket()
port = 8080
host = input(str('Please enter the server address: '))
s.connect((host,port))
print('')
print('Connected to the server successfully')
print('')


while 1:
    command = s.recv(1024)
    command = command.decode()
    if command == 'view_cwd':
        files = os.getcwd()
        files = str(files)
        