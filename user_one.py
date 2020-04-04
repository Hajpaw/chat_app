import socket

addr = ("", 16230)
recData = bytearray([])

print('server created')
serv = socket.create_server(addr)
input()