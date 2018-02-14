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
    t = dt * np.arange(0, n+1)

    X_out = X(f_x, a_x, t)
    Y_out = Y(f_y, a_y, t, phi)
    Z_out = Z(X_out, Y_out)

    return X_out, Y_out, Z_out

# ---------
# Constants
# ---------
a_x = 1
a_y = 1
phi = 0.1
dt = 0.001
n = 1000

fig, ((p1, p2), (p3, p4)) = plt.subplots(2, 2)
plots = [p1, p2, p3, p4]

for i in range(4):
    f_x = random.randint(1, 10)
    f_y = random.randint(1, 10)
    results = trig_np(f_x, f_y, a_x, a_y, phi, dt, n)
    title = f'$f_x = {f_x}, f_y = {f_y}$'
    plots[i].plot(results[1], results[0])
    plots[i].set_title(title)

p3.set_xlabel('$Y(t)$') 
p4.set_xlabel('$Y(t)$')

p1.set_ylabel('$X(t)$')
p3.set_ylabel('$X(t)$') 

plt.tight_layout()
plt.show()





