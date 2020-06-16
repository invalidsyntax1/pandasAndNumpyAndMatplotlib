#!/usr/bin/env python
# coding: utf-8
import numpy



#создание numpy массива напрямую
arr1 = numpy.arange(10) # создаёт массив от 1 до 9
arr2 = numpy.arange(0,10,2) # создаёт массив от 1 до 9 с шагом 2
arr3 = numpy.zeros(5) # создаёт массив состоящий из 5 нулей
arr4 = numpy.zeros((2, 3)) # создаёт двумерный массив состоящий из нулей, в массиве два других массива в каждом из которых по 3 нуля
arr5 = numpy.full((2,3), 8) # создаёт двумерный массив состоящий из восьмёрок, в массиве два других массива в каждом из которых по 3 восьмёрки, можно заменить 8 на любое число, которое и будет заполнено в массивах
arr6 = numpy.eye(14) # сам не понял, просто оставлю это здесь: Sometimes, you need to create an array that mirrors an identity matrix. In
#NumPy, you can do so using the eye() function, типо единичную матрицу составляет
arr7 = numpy.random.random((2,4)) # создаёт массив в котором 2 массива и в каждом из массивов по 4 случайных числа
arr8 = numpy.full(10, 8) # создаёт массив с 10тью восьмёрками


#создание numpy массива после того, как был создан обычный массив
com_list = [1,2,3,4,5] 
arr_nump = numpy.array(com_list)


#вывод результатов
print(arr1) #вывод массива
print(arr1.shape) #вывод длины массива
print(arr2) #вывод массива
print(arr2.shape) #вывод длины массива
print(arr3) #вывод массива
print(arr3.shape) #вывод длины массива
print(arr4) #вывод массива
print(arr4.shape) #вывод длины массива
print(arr5) #вывод массива
print(arr5.shape) #вывод длины массива
print(arr6) #вывод массива
print(arr6.shape) #вывод длины массива
print(arr7) #вывод массива
print(arr7.shape) #вывод длины массива
print(arr_nump) #вывод массива
print(arr_nump.shape) #вывод длины массива
print(arr8) #вывод массива
print(arr8.shape) #вывод длины массива


