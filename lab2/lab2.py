import re
import subprocess
from math import *
import pathlib
import shutil
import glob
import re
import hashlib
import os
import sys
import datetime
import time


# Напишите скрипт, который читает текстовый файл и выводит символы
# в порядке убывания частоты встречаемости в тексте.

def ex1():
    try:
        with open(r'.\test1.txt', 'r') as file:
            text = file.read().replace(' ', '').replace(',', '').replace('.', '').replace('-', '').lower()
            count_symb = {i:text.count(i) for i in text}
            print(count_symb, '\n', [i[0] for i in sorted(count_symb.items(), reverse=True)], '\n')
    except FileNotFoundError:
        print('ERROR! File not found!')


# Напишите скрипт, позволяющий искать в заданной директории и в ее
# подпапках файлы-дубликаты на основе сравнения контрольных сумм
# (MD5). Файлы могут иметь одинаковое содержимое, но отличаться
# именами. Скрипт должен вывести группы имен обнаруженных файловдубликатов.


def ex2():
    curr_path = os.getcwd()
    file_hash = dict()

    for files in os.listdir(curr_path):
        if os.path.isfile(files):
            with open(files, "rb") as file:
                file_hash.setdefault(hashlib.md5(file.read()).digest(), []).append(file.name)
    print(str([file_hash[f_name] for f_name in file_hash if len(file_hash[f_name]) > 1]).replace('[', '').replace(']', ''), '\n')


# Задан путь к директории с музыкальными файлами (в названии
# которых нет номеров, а только названия песен) и текстовый файл,
# хранящий полный список песен с номерами и названиями в виде строк
# формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
# имена файлов в директории на основе текста списка песен.


def ex3():
    path = './test_3'

    try:
        if not os.path.exists(path):
            raise Exception('Error: Folder not found')
        with open('./test_3.txt', 'r', encoding='utf-8') as names:
            for file in os.listdir(path):
                os.rename(path + '/' + file, path + '/' + names.readline().rstrip() + '.mp3')
    except FileNotFoundError:
        print('ERROR! File not found!')


# . Напишите скрипт, который позволяет ввести с клавиатуры имя
# текстового файла, найти в нем с помощью регулярных выражений все
# подстроки определенного вида, в соответствии с вариантом.
# вариант 3: найдите все IPv4-адреса – подстроки вида «192.168.5.48».


def get_file(file_name):
    if os.path.exists(os.getcwd() + '\\' + file_name):
        with open(file_name, 'r') as file:
            text = [i for i in file]
        return text


def get_substrings(text, expr):
    for str_index in range(len(text)):
        curr_count = 0
        curr_substr = re.search(expr, text[str_index])

        while curr_substr != None:
            yield str_index + 1, curr_substr.regs[0][0] + curr_count + 1, curr_substr.group
            curr_count += curr_substr.regs[0][1]
            text[str_index] = text[str_index][curr_substr.regs[0][1]:]
            curr_substr = re.search(expr, text[str_index])


def ex4():
    expr = r'^((25[0-5]|2[4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[4]\d|[01]?\d\d?)$'
    output = 'Строка №{0}, позиция: {1} - найдено [{2}]'

    try:
        text = get_file(input('Enter file-name: '))
        print([output.format(line, pos, substr) for line, pos, substr in get_substrings(text, expr)])
    except FileNotFoundError:
        print('ERROR! File not found!')


# Введите с клавиатуры текст. Программно найдите в нем и выведите
# отдельно все слова, которые начинаются с большого латинского
# символа (от A до Z) и заканчиваются 2 или 4 цифрами.


def ex5():
    expr = r'[A-Z][A-Za-z]+([0-9]{2}$|[0-9]{4}$)'
    text = input('Enter text: ')
    print([str(substr) for line, pos, substr in get_substrings(text, expr)])


# Напишите скрипт reorganize.py, который в директории --source создает
# две директории: Archive и Small. В первую директорию помещаются
# файлы с датой изменения, отличающейся от текущей даты на
# количество дней более параметра --days (т.е. относительно старые
# файлы). Во вторую – все файлы размером меньше параметра --size байт.
# Каждая директория должна создаваться только в случае, если найден
# хотя бы один файл, который должен быть в нее помещен.


def get_last_change_time(path, days):
    return datetime.datetime.fromtimestamp(os.path.getmtime(path))


def main(path=sys.path[0], days=2, size=4096):
    if os.path.isdir(path) and not os.path.exists(path):
        print('ERROR!!! Path is not found!')

    path_archive = path + '\\' + 'Archive'
    path_small = path + '\\' + 'Small'
    path_clear = path + '\\'
    to_archive, to_small = False

    if os.path.isdir(path_archive):
        to_archive = True

    if os.path.isdir(path_small):
        to_small = True

    cur_date = datetime.datetime.today()

    files_list = os.listdir(path)

    for file in files_list:
        if os.path.isfile(path_archive + file) and cur_date - get_last_change_time(
                path_clear + file) >= datetime.timedelta(days=days):
            if to_archive:
                os.mkdir(path_archive)
                to_archive = False
            shutil.copy(path_clear + file, path_archive + '\\' + file)

        if os.path.isfile(path_clear + file) and os.path.getsize(path_clear + file) <= size:
            if to_small:
                os.mkdir(path_small)
                to_small = False
            shutil.copy(path_clear + file, path_small + '\\' + file)


if __name__ == '__main__':
    if len(sys.argv) == 7 and sys.argv[1] == '--sourse' and sys.argv[3] == "--days" and sys.argv[5] == '--size':
        main(sys.argv[2], int(sys.argv[4]), int(sys.argv[7]))
    else:
        raise Exception('ERROR!!! Incorrect command or something else went wrong!')


    def ex6():
        os.mkdir(r'D:\\Lab2Test')
        subprocess.call('reorganize.py --sourse \'D:\\Lab2Test\' --days 2 --size 4096', shell=True)



def main():
    ex1()


main()