#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy


# In[10]:


com_arr = [1,2,3,4,7]
num_arr = numpy.array(com_arr)
a = num_arr > 2 # а = списку в виде True/False где, если число в num_arr больше двух, то он True, иначе False
b = num_arr[num_arr > 2] # b = списку из чисел, которые в списке num_arr больше двух
np_arr = numpy.arange(20) #создание массива от 1 до 19
even_num = np_arr[np_arr % 2 == 0] # even_num = чётным числам в массиве np_arr


# In[11]:


print(a)
print(b)
print(np_arr)
print(even_num)

