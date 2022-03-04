"""
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт,
автоматизирующий его заполнение данными.
"""


import json
from lesson02.task1 import get_encoding
from pprint import pprint


#  Для этого:


"""
1. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
"""


def write_order_to_json(item, qty, price, buyer, date, file='orders.json', debug=False):
    # indent=4
    order = {
        'item': item,
        'quantity': qty,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    enc = get_encoding(file, debug=True)

    with open(file, 'r', encoding=enc) as in_file:
        json_obj = json.load(in_file)

        if debug:
            print('BEFORE')
            print(json_obj)
            print('=' * 20, '\nAFTER:')
        # Важно! Не перезаписать, а добавить к списку УЖЕ имеющихся заказов!
        json_obj['orders'].append(order)
        if debug:
            pprint(json_obj)

    with open(file, 'w', encoding='utf-8') as out_file:
        json.dump(json_obj, out_file, ensure_ascii=False, indent=4)
        # out_file.write(json_out)



"""
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""


write_order_to_json('Принтер струйный HP DeskJet', 100, 2500, 'МегаПродавец', '20-02-2022')
write_order_to_json('Принтер матричный Maxton', 4, 75000, 'Магазин ненужного хлама', '27-01-2022', debug=True)
