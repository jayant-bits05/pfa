# -*- coding: utf-8 -*-
"""stat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1emiFubF_1KxTdwLaCpmTFqvO4hEqUmwl
"""

def mean(x):
  """"this function give avg of list or tupple"""
  temp =0
  for i in x :
    temp = i + temp
  return temp/len(x)

def median(x):
  """"this function give mod of list or tupple"""
  n=len(x)
  if n % 2 == 0:
    median1 = x[n//2]
    median2 = x[n//2 - 1]
    return (median1 + median2)/2
  else:
    median = x[n//2]
    return median

