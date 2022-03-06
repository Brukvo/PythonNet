from socket import socket, AF_INET, SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 8888))
raw_time = client.recv(1024).decode('utf-8').strip().split(' ')
for item in raw_time:
    if item == '':
        raw_time.remove(item)
print(f'Текущее время: {raw_time}')
client.close()

