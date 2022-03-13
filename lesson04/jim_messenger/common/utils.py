import sys, os
sys.path.append(os.path.join(os.getcwd(), '..'))
from common import vars
import json


def get_msg(client):

    raw_response = client.recv(vars.MAX_PACKAGE_LEN)
    if isinstance(raw_response, bytes):
        json_response = raw_response.decode(vars.ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send(sock, msg):
    if not isinstance(msg, dict):
        raise TypeError
    json_msg = json.dumps(msg)
    sock.send(json_msg.encode(vars.ENCODING))


def s_response(message):
    if vars.ACTION in message and message[vars.ACTION] == vars.PRESENCE and vars.TIME in message \
            and vars.USER in message and message[vars.USER][vars.ACCOUNT_NAME] == 'Guest':
        return {vars.RESPONSE: 200}
    return {
        vars.RESPONSE: 400,
        vars.ERROR: 'Bad Request'
    }


def compose(c_socket, msg):
    pass
