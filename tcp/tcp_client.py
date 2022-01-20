import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8888))
sock.send(b'Pornhub is closed')
sock.close()
