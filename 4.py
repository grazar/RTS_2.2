import numpy as np
from random import *
from math import sin, cos, pi
import matplotlib.pyplot as plt
import time

n = 8  
w = 1500
N = 1024
number = w/(n - 1)

w_values = [w - n * number for n in range(n)]
x = np.zeros(N)

for j in range(n):
    amp = choice([i for i in range(-10, 10) if i != 0])
    fi = randint(-360, 360)
    for i in range(N):
        x[i] += amp * sin(w_values[j] * i + fi)

coeff = np.zeros(shape=(N//2, N//2))
for i in range(N//2):
    for j in range(N//2):
        coeff[i][j] = cos(4*pi/N * i * j) + sin(4*pi/N * i * j)

coeff_N = np.zeros(N)
for i in range(N):
    coeff_N[i] = cos(2*pi/N * i) + sin(2*pi/N * i)

F1 = np.zeros(N//2)
F2 = np.zeros(N//2)
F = np.zeros(N)

for i in range(N//2):
    for j in range(N//2):
        F2[i] += x[2*j] * coeff[i][j]
        F1[i] += x[2*j + 1] * coeff[i][j]


for i in range(N):
    if i < (N//2):
        F[i] += F2[i] + coeff_N[i] * F1[i]
    else:
        F[i] += F2[i - (N//2)] - coeff_N[i] * F1[i - (N//2)]

plt.ylabel('X')
xpl = plt.plot(x)
plt.grid()
plt.savefig("X.png")
plt.clf()
phase = plt.plot(F)
plt.ylabel('F')
plt.grid()
plt.savefig("F.png")