#!/usr/bin/env python
# coding: utf-8

import numpy


x1 = numpy.array([[1,2,3],[4,5,6]])
y1 = numpy.array([[7,8,9],[2,3,4]])
sum_x1_y1 = x1 + y1 #числа нулевого массива сложатся с числами нулевого, числа единичного с числами единичного и т.д.
#Математика массива важна, поскольку она может использоваться для выполнения векторных вычислений.
#Хороший пример таков:
x = numpy.array ([2,3])
y = numpy.array ([4,2])
z = x + y #также можно использовать функцию add: z = numpy.add(x,y)
#смотри картинку
dif_x1_y1 = x1 - y1 # то же самое что и numpy.subtract(x1,y1)
product_x1_y1 = x1 * y1 #то же самое что и numpy.multiply(x1,y1)
div_x1_y1 = x1 / y1 #то же самое что и numpy.divide(x1,y1)
#Какая практическая польза от умножения или деления двух массивов? Как
#Например, предположим, у вас есть три массива: один, содержащий имена группы
#людей, другой соответствующие высоты этих людей, и последний
#один соответствующий вес отдельных лиц в группе:
names = numpy.array(['Ann','Joe','Mark'])
heights = numpy.array([1.5, 1.78, 1.6])
weights = numpy.array([65, 46, 59])
bmi = weights/heights **2 # bmi = [28.88888889 14.51836889 23.046875  ]


print(sum_x1_y1)
print(z)
print(dif_x1_y1)
print(product_x1_y1)
print(div_x1_y1)
print(bmi)
print("Overweight: " , names[bmi>25])
print("Underweight: " , names[bmi<18.5])
print("Healthy: " , names[(bmi>=18.5) & (bmi<=25)])

