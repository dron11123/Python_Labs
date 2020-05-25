import math
import datetime
import random
import itertools
from math import *
import numbers
import enum
import time

msg_text = 'Enter the text: '


# Напишите скрипт, который преобразует введенное с клавиатуры
# вещественное число в денежный формат.


def ex1():
    summ = input('Enter sum: ').replace(',', '.').split('.')
    if int(summ[0]) < 0:
        raise Exception('ERROR! Incorrect format!')
    else:
        print(summ[0] + ' руб. ' + summ[1] + ' коп.')


# Написать скрипт, который выводит на экран «True», если элементы
# программно задаваемого списка представляют собой возрастающую
# последовательность, иначе – «False».  


def ex2():
    spisok = [i for i in input('Add numbers: ').split(' ')]
    print(True) if [i for i in range(len(spisok) - 1) if spisok[i] <= spisok[i + 1]] else print(False)


# Напишите скрипт, который позволяет ввести с клавиатуры номер
# дебетовой карты (16 цифр) и выводит номер в скрытом виде.  


def ex3():
    length = 16

    card = input('Enter card-number: ').replace(' ', '').replace('-', '')
    print(card[:4] + '*' * 8 + card[12:length]) if len(card) == length else print('ERROR! Incorrect format!')


# Напишите скрипт, который разделяет введенный с клавиатуры текст на
# слова и выводит сначала те слова, длина которых превосходит 7
# символов, затем слова размером от 4 до 7 символов, затем – все
# остальные.


def ex4():
    text = input(msg_text).split(' ')
    print('Length > 7: {0}\n'.format([i for i in text if len(i) > 7]))
    print('Length 4 - 7: {0}\n'.format([i for i in text if len(i) >= 4 and len(i) <= 7]))
    print('Length <= 4: {0}\n'.format([i for i in text if len(i) < 4]))


# Напишите скрипт, который позволяет ввести с клавиатуры текст
# предложения и сформировать новую строку на основе исходной, в
# которой все слова, начинающиеся с большой буквы, приведены к
# верхнему регистру.


def ex5():
    text = input('Enter text:').split(' ')
    print(' '.join([i.upper() if i == i.title() else i for i in text]))


# Напишите программу, позволяющую ввести с клавиатуры текст
# предложения и вывести на консоль все символы, которые входят в этот
# текст ровно по одному разу.


def ex6():
    text = input(msg_text)
    print('Unique symbols:', ', '.join([i for i in text if text.count(i) == 1]))


# Напишите скрипт, который обрабатывает список строк-адресов
# следующим образом: сначала определяет, начинается ли каждая строка
# в списке с префикса «www». Если условие выполняется, то скрипт
# должен вставить в начало этой строки префикс «http://», а затем
# проверить, что строка заканчивается на «.com». Если у строки другое
# окончание, то скрипт должен вставить в конец подстроку «.com».


def ex7():
    url = ['www.vk.com', 'habr.com', 'www.vk', 'Animevost.org']
    changed = ['http://' + i if ('www.' in i) else 'http://www.' + i for i in url]
    print([i + '.com' if (not '.com' in i) else i for i in changed])


# Напишите скрипт, генерирующий случайным образом число n в
# диапазоне от 1 до 10000. Скрипт должен создать массив из n целых
# чисел, также сгенерированных случайным образом, и дополнить
# массив нулями до размера, равного ближайшей сверху степени двойки.


def ex8():
    array = [int(random.uniform(1, 1000)) for i in range(0, int(random.uniform(1, 10000)))]
    new_size = 2 ** math.ceil(math.log2(len(array)))

    print('Size before: {0}\n'.format(len(array)))
    [array.append(random.uniform(1, 1000)) for i in range(len(array), new_size)]
    print('Size after: {0}\n'.format(len(array)))


# . Напишите программу, имитирующую работу банкомата. Выберите
# структуру данных для хранения купюр разного достоинства в заданном
# количестве. При вводе пользователем запрашиваемой суммы денег,
# скрипт должен вывести на консоль количество купюр подходящего
# достоинства. Если имеющихся денег не хватает, то необходимо
# напечатать сообщение «Операция не может быть выполнена!».
# Например, при сумме 5370 рублей на консоль должно быть выведено
# «5*1000 + 3*100 + 1*50 + 2*10».


def print_banc(bank):
    return bank[1000] * 1000 + bank[500] * 500 + bank[100] * 100 + bank[50] * 50 + bank[10] * 10


def get_banc(bank, summ):
    for nominal in bank:
        _take = int(summ / nominal) // 1 if int(summ / nominal) // 1 <= bank[nominal] else bank[nominal]
        summ -= _take * nominal
        bank[nominal] = _take
    print(str(bank).replace(': ', '*').replace(', ', ' + '))


def ex9():
    bank = {1000: 20, 500: 10, 100: 10, 50: 10, 10: 10}
    print('Bank summ: {0}\nBank: {1}'.format(print_banc(bank), bank))

    money = int(input('Enter summ: '))
    if money > print_banc(bank):
        raise Exception('ERROR! Operation can\'t be executed!')
    get_banc(bank, money)


# Напишите скрипт, позволяющий определить надежность вводимого
# пользователем пароля. Это задание является творческим: алгоритм
# определения надежности разработайте самостоятельно.


def check(password):
   if len(password) < 4:
       print('Error: too short')
   if password == 'MY DICK':
       print('Error: too short')
   if password.isdigit():
       print('Error: need some letters')
   if len(password) > 4 and not password.isdigit():
       print('Best password in the world')



def ex10():
    password = input('Create password ')
    check(password)


# Написать генератор frange как аналог range с дробным шагом

def frange(start, end, step):
    while start <= (end - step):
        yield float('{:.1f}'.format(start + step))
        start += step


def ex11():
    for x in frange(1, 5, 0.1):
        print(x)


# Напишите генератор get_frames(), который производит «оконную
# декомпозицию» сигнала: на основе входного списка генерирует набор
# списков – перекрывающихся отдельных фрагментов сигнала размера
# size со степенью перекрытия overlap.


def get_frames(signal, size, overlap):
    show_len = int(size * overlap)
    curr_step = 0

    while curr_step < len(signal) - 1:
        yield signal[curr_step: curr_step + size]
        curr_step += show_len


def ex12():
    try:
        slen = int(input('Enter length of signal: '))
        signal = [i for i in range(slen)]

        for frame in get_frames(signal, 4, 0.5):
            print(frame)
    except ValueError:
        print('ERROR! Incorrect format')


# 13. Напишите собственную версию генератора enumerate под названием
# extra_enumerate. Пример вызова:
# for i, elem, cum, frac in extra_enumerate(x):
#  print(elem, cum, frac)
# 5
# В переменной cum хранится накопленная сумма на момент текущей
# итерации, в переменной frac – доля накопленной суммы от общей
# суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
# вывод будет таким:
#  (1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1).


def extra_enumerate(x):
    temp = 0
    for i in x:
        temp += i
        yield i, temp, temp / sum(x)


def ex13():
    x = [1, 3, 4, 2]
    for elem, summ, frac in extra_enumerate(x):
        print(elem, summ, frac)


# . Напишите декоратор non_empty, который дополнительно проверяет
# списковый результат любой функции: если в нем содержатся пустые
# строки или значение None, то они удаляются.


def non_empty(returned_func):
    def wrap():
        returned = returned_func()
        deleted = 0

        for i in returned:
            if i is None or i == '':
                returned.pop(deleted)
            deleted += 1
        return returned

    return wrap


@non_empty
def getList():
    return ['chapter1', '', 'contents', '', 'line1']


def ex14():
    print(getList())


# Напишите параметризированный декоратор pre_process, который
# осуществляет предварительную обработку (цифровую фильтрацию)
# списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в
# коде (по умолчанию равен 0.97).


def pre_process(a):
    def decor(returned_func):
        def wrap(*args):
            s = args[0]
            for i in range(len(s)):
                s[i] = s[i] - a * s[i - 1]
                print('a = {0}'.format(a))
                returned_func(s)

        return wrap

    return decor


@pre_process(a=0.95)
def plot_signal(s):
    for sample in s:
        print(sample)


def ex15():
    signal = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    plot_signal(signal)


# Напишите скрипт, который на основе списка из 16 названий
# футбольных команд случайным образом формирует 4 группы по 4
# команды, а также выводит на консоль календарь всех игр (игры
# должны проходить по средам, раз в 2 недели, начиная с 14 сентября
# текущего года). Даты игр необходимо выводить в формате «14/09/2016,
# 22:45». Используйте модули random и itertools.

def ex16():
    teamList = [
        'Живое пиво', 'Пари Сен-Жермен', 'Манчестер Юнайтед', 'Наполи',
        'Алюминий', 'Бавария', 'Галатасарай', 'Милан',
        'Бельмопанские бандиты', 'Интер', 'Баруссия Дортмунд', 'Химнасия де Хухуй',
        'Боруссия', 'Атлетико Мадрид', 'Лион', 'Цемент'
    ]
    playDate = datetime.datetime(2020, 9, 14, 22, 45)

    random.shuffle(teamList)
    groups = [teamList[i * 4:i * 4 + 4] for i in range(4)]
    [print('Group #:', i + 1, ' - ', groups[i]) for i in range(len(groups))]

    for i in range(len(teamList)):
        print("Game #:", i, playDate.strftime("%d/%m/%Y %H:%M"))
        playDate += datetime.timedelta(days=14)


def main():
    exersices = {1: ex1(), 2: ex2(), 3: ex3(), 4: ex4(), 5: ex5(), 6: ex6(), 7: ex7(), 8: ex8(),
                 9: ex9(), 10: ex10(), 11: ex11(), 12: ex12(), 13: ex13(), 14: ex14(), 15: ex15(), 16: ex16()}

    for i in exersices.keys():
        exersices[i]

main()