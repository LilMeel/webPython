import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOCK_STREAM - TCP-протокол
sock.bind(("localhost",8888))
sock.listen(5)
# Размер очереди, кол-во соединений. Пришло 6 соединений
# одно мы обрабатываем, а 5 в очереди

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print("I'm fine! (not at all)",result.decode("utf-8"))