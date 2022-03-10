 
"""
Для проверки решения в качестве аргументов этих функций следует использовать указаные в задачах значения. При решении
задач необходимо также избегать дублирования кода и помнить о правилах PEP-8.
"""

import chardet
import subprocess
import platform


WORDS = {
    'unicode': ['разработка', 'сокет', 'декоратор', r'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                r'\u0441\u043e\u043a\u0435\u0442', r'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'],
    'bytes': [b'class', b'function', b'method'],
    'byte_check': ['attribute', 'класс', 'функция', 'type'],
    'trans': ['разработка', 'администрирование', 'protocol', 'standard']
}

# Задание 1
"""
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и
также проверить тип и содержимое переменных.
"""
print(f"{' Задание 1 ':-^40}")
words_1 = WORDS['unicode']
for el in range(3, 6):
    print(f"Слово: {words_1[el-3]}, тип: {type(words_1[el-3])}, Unicode: {words_1[el]}, тип: {type(words_1[el])}")
del words_1

# Задание 2
"""
Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом, а не
ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы encode,
decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.
"""
print(f"\n\n{' Задание 2 ':-^40}")
words_2 = WORDS['bytes']
for word in words_2:
    print(f"Тип: {type(word)}, содержимое: {word}, длина: {len(word)}")
del words_2

# Задание 3
"""
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе. Важно: решение
должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""

print(f"\n\n{' Задание 3 ':-^40}")
non_byte, words_3 = [], WORDS['byte_check']
for word in words_3:
    try:
        print(f'Попытка преобразования в байты слова "{word}"...', end='')
        word.encode('ascii')
        print('✔', end='\n')
    except UnicodeEncodeError:
        print('❌', end='\n')
        non_byte.append(word)

print('\nСлова, которые не удалось перевести в байты:')
print(', '.join(non_byte))
del non_byte, words_3

# Задание 4
"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""
print(f"\n\n{' Задание 4 ':-^40}")
words_4 = WORDS['trans']
for word in words_4:
    print(f'\nИсходное слово: {word}')
    trans_b = word.encode("utf-8")
    print(f'Кодированное слово: {trans_b}')
    print(f'Расшифрованное слово: {trans_b.decode("utf-8")}')

# Задание 5
"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
на кириллице.
"""

args = '-n' if platform.system().lower() == 'windows' else '-c'
ping_res = ['youtube.com', 'yandex.ru']
for res in ping_res:
    cmd = ['ping', args, '5', res]
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in process.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            line_dec = line.decode('utf-8').split()
            if 'data.' in line_dec:
                print(f'\nПинг ресурса {res}, пакетов: {cmd[2]}')
                print('-' * 20)
            elif 'from' in line_dec:
                b_count = line_dec[0]
                addr = line_dec[3]
                ttl = line_dec[6].replace('ttl=', '')
                pingtime = line_dec[7].replace('time=', '')
                print(f'{b_count} байт отдано с {addr}, TTL: {ttl}, время ответа: {pingtime} мс')
            elif 'loss,' in line_dec:
                print(f'Статистика пинга ресурса {res}:')
                print(f'Отправлено {cmd[2]}, вернулось {line_dec[3]}, потери: {line_dec[5]}, время: {line_dec[9]}\n')
        print('#' * 20)
    except FileNotFoundError:
        print('В системе не установлено приложение ping.')
        print('Установите пакет iputils через ваш пакетный менеджер.')
        break

# Задание 6
"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в неизвестной
кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.
"""
with open('test_file.txt', 'rb') as file_enc:
    content = file_enc.read()
encoding = chardet.detect(content)['encoding']
print('Предполагаемая кодировка: ', encoding)
with open('test_file.txt', encoding=encoding) as file_dec:
    for line in file_dec:
        print(line, end='')
    print()
