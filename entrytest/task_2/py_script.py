"""
Бонус к заданию
Программа в фоне считает до десяти и записывает результаты в log.txt
Для работы программы log.txt не должен быть пустым
"""
from time import sleep


def infinity_iter(num: int) -> int:
    """
    Бесконечный итератор
    :return: int
    """
    while True:
        num += 1
        yield num


while True:
    try:
        fp = open('log.txt', mode='r+')
        num = int(fp.read()[-1])
        fp.write(str(next(infinity_iter(num))))
    except:
        print('Проинициализируйте файл log.txt ')
    sleep(1)
