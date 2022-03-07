from socket import socket, AF_INET, SOCK_STREAM

days = {
	'Mon': 'понедельник'
}

months = {
	'Mar': 'марта'
}

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 8888))
raw_time = client.recv(1024).decode('utf-8').strip().split(' ')
for item in raw_time:
    if item == '':
        raw_time.remove(item)
print(f'Текущее время: {raw_time}')
print(f'Или так: {days[raw_time[0]]}, {raw_time[2]} {months[raw_time[1]]} {raw_time[4]} г., {raw_time[3]}')
client.close()

