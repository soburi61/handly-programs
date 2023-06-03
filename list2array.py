"""
Created on Sun Jun  4 00:21:50 2023
coding: utf-8

"""

import numpy as np

def list2array(lst,rows):
    # リストを2行のNumPy配列に変換します
    array = np.array(lst)
    cols = len(lst) // rows
    reshaped_array = array.reshape(rows, cols)
    return reshaped_array