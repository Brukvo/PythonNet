"""
Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
"""
# КЛИЕНТСКАЯ ЧАСТЬ

# клиент отправляет запрос серверу

# Клиент и сервер должны быть реализованы в виде отдельных скриптов,
# содержащих соответствующие функции. Функции клиента: сформировать presence-сообщение; отправить сообщение серверу;
# получить ответ сервера; разобрать сообщение сервера; параметры командной строки скрипта
# client.py <addr> [<port>]: addr — ip-адрес сервера; (по умолчанию 127.0.0.1); port — tcp-порт на сервере,
# (по умолчанию 7777).

import sys, os
sys.path.append(os.path.join(os.getcwd(), '..'))
import argparse
import json
from socket import socket, AF_INET, SOCK_STREAM
from common.vars import *
from common import utils
import time


def main(s_addr, s_ip):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((s_addr, s_ip))
    bonjour = presence()
    utils.send(client, bonjour)
    try:
        answer = utils.s_response(utils.get_msg(client))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось обработать сообщение.')


def presence(acc_name='Guest', unittest=False):
    out_time = time.time()
    if unittest:
        out_time = 1646660089.3014915
    out = {
        ACTION: PRESENCE,
        TIME: out_time,
        USER: {
            ACCOUNT_NAME: acc_name
        }
    }

    return out


def send():
    pass


def get_response():
    pass


def parse_resp(s_resp):
    if RESPONSE in s_resp:
        if s_resp[RESPONSE] == 200:
            return '200: OK'
        return f'400: {s_resp[ERROR]}'


if '__main__':
    # инициализируем и разбираем параметры с помощью argparse (надстройка над sys.argv)
    # обработку параметров argparse берёт на себя
    p = argparse.ArgumentParser()
    p.add_argument("-a", default='localhost', help='IP-адрес для прослушивания')
    p.add_argument("-p", type=int, default=7777, help='порт для прослушивания')
    args = p.parse_args()

    # при необходимости можно обратиться к параметрам напрямую:
    # print(args.a, args.p)

    print('Запускаем сервер...')
    main(args.a, args.p)
