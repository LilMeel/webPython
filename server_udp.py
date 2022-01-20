import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# AF_INET - используем IP-protocol версии 4, AF_INET6 - IPv6
# SOCK_DGRAM используем UDP-protocol
sock.bind(("127.0.0.1",8888))
# Резервирование порта на нашей машине, передаём кортеж
result = sock.recv(1024)
# Принимаем 1024 байта (зависит от сообщения и его размера)
print('Message', result.decode("utf-8"))
sock.close()