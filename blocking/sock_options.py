import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind("localhost",8888)
sock.listen(5)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

