# -*- coding: utf-8 -*-
import sys
"""
Подсчет площади покрывающей прямоугольниками. Сделан на основе
Line Sweep Algorithm
https://www.topcoder.com/tc?module=Static&d1=tutorials&d2=lineSweep
Работает не только с целыми числами, но и с вещественными
"""


def makeSortedIntervals(rects, xy):
    """ Нужна для создания массива точек - начала и конца интервала,
    сортированных по возрастанию либо по х либо по y зависит от
    соответственно xy: либо 0 либо 1
    """
    verts = []
    for rect in rects:
        verts.extend([(rect[xy], rect, 'in'), (rect[xy+2], rect, 'out')])
    verts.sort(key=lambda x: x[0])
    return verts


def calculeteArea(filename='input_1.txt'):
    f = open(filename, 'r')
    rects = [map(float, x.split(' ')) for x in f]
    rectsInterval = makeSortedIntervals(rects, 0)
    activeRect = []
    lastX = S = 0
    # В этом цикле нет проверки на то что между точками интервала
    # нет прямоугольника, потому что в этом случае Ly = 0
    for intervalX in rectsInterval:
        activeRectInterval = makeSortedIntervals(activeRect, 1)
        Ly = lastY = stackY = 0
        for intervalY in activeRectInterval:
            if stackY > 0:
                Ly = Ly + intervalY[0]-lastY
            if intervalY[2] is 'in':
                stackY = stackY+1
            else:
                stackY = stackY-1
            lastY = intervalY[0]
        if intervalX[2] is 'in':
            activeRect.append(intervalX[1])
        else:
            activeRect.remove(intervalX[1])
        S = S + (intervalX[0] - lastX)*Ly
        lastX = intervalX[0]
    return S

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print calculeteArea(sys.argv[1])
    else:
        print calculeteArea()
