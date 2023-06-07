"""
Created on Sun Jun  4 00:04:12 2023
coding: utf-8

"""
import numpy as np

A=np.array([[2,3],[7,8]])
B=np.array([[13,12,13,24],[14,14,4,24]])
R=np.dot(A,B)
R=np.array([[35,-21],[-21,7]])
R=np.mod(R,29)
print(R)
