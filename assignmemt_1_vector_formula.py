# -*- coding: utf-8 -*-
"""Assignmemt - 1_Section Formula.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12zzlQYII6z1R3XJ_GHn0n0hks7WJCI0u
"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([-3,3,-5,1])

plt.axis('on')
plt.grid(True)

A = np.array([-2, -2])
B = np.array([2, -4])
P = np.array([-0.28,-2.85])

def plot_line(p,q):
  len =10
  dim = A.shape[0]
  x_pq = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = p + lam_1[i]*(q-p)
    x_pq[:,i]= temp1.T
  return x_pq

#Generating all lines
x_AP = plot_line(A, P)
x_PB = plot_line(P, B)

#Plotting all lines
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_PB[0,:],x_PB[1,:],label='$PB$')


plt.savefig('line.png')
plt.show()