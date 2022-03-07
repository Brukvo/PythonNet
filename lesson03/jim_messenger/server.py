"""
Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
"""
# СЕРВЕРНАЯ ЧАСТЬ

# сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
# содержащих соответствующие функции.

# Функции сервера: принимает сообщение клиента; формирует ответ клиенту; отправляет ответ клиенту;
# имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777); -a <addr> — IP-адрес
# для прослушивания (по умолчанию слушает все доступные адреса).

# все переменные с префиксом s_ относятся к серверу, с префиксом c_, соответственно, к клиенту

import argparse
import json
import common
from common import vars, utils
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


def loop(s_ip, s_port):
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((s_ip, s_port))

    server.listen(vars.MAX_CONN)

    while True:
        c_socket, c_addr = server.accept()
        try:
            income_msg = utils.get_msg(c_socket)
            print(income_msg)
            answer = utils.s_response(income_msg)
            utils.send(c_socket, answer)
            server.close()
        except (ValueError, json.JSONDecodeError):
            print('Пришло некорректное сообщение.\nОстановка сервера...')
            server.close()


if '__main__':
    # инициализируем и разбираем параметры с помощью argparse (надстройка над sys.argv)
    # обработку параметров argparse берёт на себя
    p = argparse.ArgumentParser()
    p.add_argument("-a", default='', help='IP-адрес для прослушивания')
    p.add_argument("-p", type=int, default=7777, help='порт для прослушивания')
    args = p.parse_args()

    # при необходимости можно обратиться к параметрам напрямую:
    # print(args.a, args.p)

    print('Запускаем сервер...')
    loop(args.a, args.p)
