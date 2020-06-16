#!/usr/bin/env python
# coding: utf-8

import numpy


#создание массива
arr1 = [1,2,3,4,5]
arr2 = numpy.array(arr1)
#создание двумерного массива
arr3 = [6,7,8,9,0]
arr4 = numpy.array([arr1, arr3])


#индексикация
a1 = arr2[0]
a2 = arr2[3]
c1 = arr2[[0,1,2]] # вывод нескольких элементов из массива
c2 = arr2[[3,4]] # вывод нескольких элементов из массива
b1 = arr4[0,0]
b2 = arr4[1,1]
b3 = arr4[1,3]


#Вывод результатов
print(a1)
print(a2)
print(arr4)
print(b1)
print(b2)
print(b3)
print(c1)
print(c2)

