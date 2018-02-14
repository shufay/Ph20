# #!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random

# ---------
# Constants
# ---------
a_x = 1
a_y = 1
phi = 0

def X(f_x, a_x, t):
    return a_x * np.cos(2 * np.pi * f_x * t)

def Y(f_y, a_y, t, phi):
    return a_y * np.sin(2 * np.pi * f_y * t + phi)

def Z(X, Y):
    return X + Y

def trig_np(f_x, f_y, a_x, a_y, phi, dt, n):
    '''
    Computes trigonometric functions X(t), Y(t) and Z(t). Stores the 
    results in numpy arrays. 
    '''
    t = dt * np.arange(0, n+1)

    X_out = X(f_x, a_x, t)
    Y_out = Y(f_y, a_y, t, phi)
    Z_out = Z(X_out, Y_out)

    return X_out, Y_out, Z_out, t

f_x = 1.0
f_y = [0.1, 0.3, 0.7, 0.9, 1.1, 1.2]
dt = 0.01
n = 2000
phi = 0

fig, ((p1, p2), (p3, p4), (p5, p6)) = plt.subplots(3, 2)
plots = [p1, p2, p3, p4, p5, p6]

for i in range(len(f_y)):
    results = trig_np(f_x, f_y[i], a_x, a_y, phi, dt, n)
    title = f'$f_x = {f_x}, f_y = {f_y[i]}$'
    plots[i].plot(results[3], results[2])
    plots[i].set_title(title)

p5.set_xlabel('$t$') 
p6.set_xlabel('$t$')

p1.set_ylabel('$Z(t)$')
p3.set_ylabel('$Z(t)$') 
p5.set_ylabel('$Z(t)$')

plt.tight_layout()
plt.show()
