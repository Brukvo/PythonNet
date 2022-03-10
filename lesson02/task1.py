import csv, chardet, re
from pprint import pprint
"""
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
"""

"""
1. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и 
поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
«Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);
"""


def get_data(files):
    raw_os_mfc, raw_os_name, raw_os_code, raw_os_build = None, None, None, None
    os_mfc, os_name, os_code, os_build = [], [], [], []
    ptn_os_mfc = re.compile('Изготовитель системы:')
    ptn_os_name = re.compile('Название ОС:')
    ptn_os_code = re.compile('Код продукта:')
    ptn_os_build = re.compile('Тип системы:')
    csv_headers = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы'
    ]
    for file in files:
        enc = get_encoding(file)
        with open(file, encoding=enc) as file_src:
            raw_data = file_src.read()
            lines = raw_data.split("\n")
            for line in lines:
                if len(ptn_os_mfc.split(line)) > 1:
                    os_mfc.append(ptn_os_mfc.split(line)[1].strip())

                if len(ptn_os_name.split(line)) > 1:
                    os_name.append(ptn_os_name.split(line)[1].strip())

                if len(ptn_os_code.split(line)) > 1:
                    os_code.append(ptn_os_code.split(line)[1].strip())

                if len(ptn_os_build.split(line)) > 1:
                    os_build.append(ptn_os_build.split(line)[1].strip())
    return csv_headers, os_mfc, os_name, os_code, os_build


def get_encoding(file, debug=False):
    with open(file, 'rb') as f:
        content = f.read()
    encoding = chardet.detect(content)['encoding']
    if debug:
        print(f'Предполагаемая кодировка: {encoding.upper()}')
    return encoding


"""
2. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
"""


def write_to_csv(raw_data):
    with open('main_data.csv', mode='w', encoding='utf-8') as out_file:
        csv.writer(out_file).writerow(raw_data[0])
        for row in range(len(raw_data[1])):
            out_line = []
            for col in range(1, len(raw_data)):
                out_line.append(raw_data[col][row])
            csv.writer(out_file).writerow(out_line)


"""
3. Проверить работу программы через вызов функции write_to_csv().
"""

write_to_csv(get_data(['info_1.txt', 'info_2.txt', 'info_3.txt']))
