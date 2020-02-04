# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 23:53:45 2020

@author: Vanshika Garg
"""
a = input("enter  the number in the list")
l= [ int(i) for i in a.split(" ") ]
b= l[ : : -1]
print (l)
print(b)
c=[]
for i in range(0,len(l)):
    c.append(l[i]+b[i])
print(c)
