"""
Created on Sun Jun  4 00:04:12 2023
coding: utf-8

"""
import numpy as np

A=np.array([[6,8],[8,7]])
B=np.array([[15,24,0,6,1],[18,27,25,10,15]])
R=np.dot(A,B)
#R=np.mod(R,29)
print(R)
