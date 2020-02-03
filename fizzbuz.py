# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:49:36 2020

@author: Vanshika Garg
"""
a = int(input("Enter the number"))
for i in range (1,a+1):
    if(i%3==0) & (i%5==0):
        print("fizzbuzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    else :
        print (i)
    