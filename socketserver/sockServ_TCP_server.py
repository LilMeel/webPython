import socketserver

class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print("Address: {}".format(self.client_address[0]))
        print("Data: {}".format(data.decode()))
        self.request.sendall(data)

if __name__ == '__main__':
    with socketserver.TCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
# Сервер отправляет тоже самое, что и принял от клиента(дописываем в клиенте):
    # result = sock.recv(64)
    # print('Response: ', result)
    # sock.close()
"""В функции server_forever уже предусмотрено ожидание,
   поэтому цикл {while True:} - не нужен"""