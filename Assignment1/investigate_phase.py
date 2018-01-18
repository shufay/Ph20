# #!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random


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
    X_out = np.array([])
    Y_out = np.array([])
    Z_out = np.array([])

    for i in range(n + 1):
        t = i * dt
        x = X(f_x, a_x, t) 
        y = Y(f_y, a_y, t, phi)
        z = Z(x, y)

        X_out = np.append(X_out, np.array(x))
        Y_out = np.append(Y_out, np.array(y))
        Z_out = np.append(Z_out, np.array(z))

    return X_out, Y_out, Z_out

# ---------
# Constants
# ---------
a_x = 1
a_y = 1
f_x = 1
f_y = 1
dt = 0.001
n = 1000
phase = [0, 1/4, 1/2, 1, 5/4, 3/2]

fig, ((p1, p2), (p3, p4), (p5, p6)) = plt.subplots(3, 2)
plots = [p1, p2, p3, p4, p5, p6]

for i, item in enumerate(phase):
    phi = item * np.pi
    results = trig_np(f_x, f_y, a_x, a_y, phi, dt, n)
    title = f'$\phi = {item} \pi$'
    plots[i].plot(results[1], results[0])
    plots[i].set_title(title)

p5.set_xlabel('$Y(t)$') 
p6.set_xlabel('$Y(t)$')

p1.set_ylabel('$X(t)$')
p3.set_ylabel('$X(t)$') 
p5.set_ylabel('$X(t)$')

plt.tight_layout()
plt.show()

