import socket
import os

unix_sock_name = 'unix.sock' # unix_sock_name: "unix.socket"
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
# Новый протокол AF_UNIX - использует в качестве точки обмена - файл

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)
# Проверка - существует ли уже такой файл. Если сущ - удаляем

sock.bind(unix_sock_name)
# Передаём уже строковое значение, а не кортеж, так как там файл

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
    else:
        print("Message", result.decode("utf-8"))
