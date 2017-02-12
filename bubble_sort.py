#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bubble_sort.py
#  
#  Copyright 2017 HP <HP@HP-PC>
#  
#  Сортировка "пузырьком" целых чисел
#  
#  
#  
#  
#
# 
#  
#  
#  
#  
#  
# 
#  
#  
#  


num_list=input('Input unsort sequence: ').split()
len_list=len(num_list)
while (len_list>1):
	for i in range(0, len_list-1):
		if int(num_list[i])>int(num_list[i+1]):
			num_list[i], num_list[i+1]=num_list[i+1], num_list[i]
		i+=1
	len_list-=1
print(num_list)
