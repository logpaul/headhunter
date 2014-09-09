# -*- coding: utf-8 -*-
import sys
from decimal import Decimal, getcontext
"""

"""
PRECISION = getcontext().prec = 800


def myAlgoritm(seq):
    """Алгоритм для выявления периода в последовательности seq, если нет
    периода то возращает seq.
    Пробовал решить эту проблему известными алгоритмом Черепахи и кролика,
    но при его скорости работы, он показывал плохие результаты на больших
    дробях типа 1/9801.
    В результате решил забить на скорость и предпочел более надежный алгоритм.
    """
    seqinv = seq[::-1]
    size = len(seq)
    l = 0
    for s in range(1, len(seqinv)//3):
        for i in range(1, 4):
            if seqinv[0:s] != seqinv[i*s:(i+1)*s]:
                break
        else:
            size = s
            break
    if size == len(seq):
        return seq
    for i in range(0, len(seq)-3*size):
        if seq[i:i+size] == seq[i+size:i+2*size]:
            l = i
            break
    return '%s(%s)' % (seq[0:l], seq[l:l+size])


def intToChar(i):
    """Для систем с основанием больше чем 10
    """
    if i < 10:
        return str(i)
    else:
        return str(unichr(i+87))


def divide(a):
    """Функция для деления числа и перевода его в другую систему
    a - массив: a[0] - числитель a[1] - знаменатель, a[2] - основание системы
    """
    def decToNFloor(n):
        s = ''
        if n == 0:
            return '0'
        for i in range(1, 10 * PRECISION//a[2]):
            if n == 0:
                return s
            else:
                s = intToChar(int(n % a[2])) + s
                n = int(n / a[2])
        return s

    def decToNFrac(n):
        s = ''
        for i in range(1, 10 * PRECISION//a[2]):
            if n == 0:
                return s
            else:
                b = int(n*a[2])
                s = s + intToChar(b)
                n = n*a[2]-b
        return s

    floor = a[0] // a[1]
    frac = a[0]/a[1] - floor
    frac = myAlgoritm(decToNFrac(frac))
    floor = decToNFloor(floor)
    return floor + '.' + frac


def calc(filename='input_2.txt'):
    """считает из файла входные данные и для каждой строчки вызывает divide
    """
    f = open(filename, 'r')
    return [map(divide, [map(Decimal, x.split(' '))]) for x in f]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = calc(sys.argv[1])
    else:
        result = calc()
    print '\n'.join(sum(result, []))
