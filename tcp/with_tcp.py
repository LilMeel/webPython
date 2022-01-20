import socket

#  С помощью оператора with прохода мы освобождаем порт
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print("8888 is bind")
    sock.bind(("localhost", 8888))

    while True:
        result = sock.recv(1024)
        print("Never Gonna Give You Up", result.decode("utf-8"))
