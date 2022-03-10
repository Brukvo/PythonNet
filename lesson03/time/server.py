from socket import socket, AF_INET, SOCK_STREAM
import time

server = socket(AF_INET, SOCK_STREAM)
server.bind(('', 8888))
server.listen()

try:
    while True:
        client, addr = server.accept()
        print(f'Получили запрос: IP={addr[0]}, порт={addr[1]}')
        now = time.ctime(time.time()) + '\n'
        client.send(now.encode('utf-8'))
        client.close()
except KeyboardInterrupt as exc:
    print('Процесс прерван пользователем.')
finally:
    server.close()
