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

# First case: 0 < f_x/f_y < 1
dt = 0.001
n = 1000
phi = 0.1
f_y = 5
ratio = [0.2, 0.4, 0.6, 0.8]

fig, ((p1, p2), (p3, p4)) = plt.subplots(2, 2)
plots = [p1, p2, p3, p4]

for i, r in enumerate(ratio):
    f_x = f_y * r
    results = trig_np(f_x, f_y, a_x, a_y, phi, dt, n)
    title = f'ratio = {r}'
    plots[i].plot(results[1], results[0])
    plots[i].set_title(title)

p3.set_xlabel('$Y(t)$') 
p4.set_xlabel('$Y(t)$')

p1.set_ylabel('$X(t)$')
p3.set_ylabel('$X(t)$') 
 
plt.suptitle('$f_x/f_y < 1$')
plt.tight_layout()

# Second case: f_x/f_y > 1
dt = 0.0001
n = 2000
phi = 1
ratio = [3, 6, 9, 12]

fig2, ((p1, p2), (p3, p4)) = plt.subplots(2, 2)
plots = [p1, p2, p3, p4]

for i, r in enumerate(ratio):
    f_x = f_y * r
    results = trig_np(f_x, f_y, a_x, a_y, phi, dt, n)
    title = f'ratio = {r}'
    plots[i].plot(results[1], results[0])
    plots[i].set_title(title)

p3.set_xlabel('$Y(t)$') 
p4.set_xlabel('$Y(t)$')

p1.set_ylabel('$X(t)$')
p3.set_ylabel('$X(t)$') 
 
plt.suptitle('$f_x/f_y > 1$')
plt.tight_layout()

# Third case: f_x/f_y irrational
dt = 0.001
n = 5000
phi = 0.1
f_y = 2

ratio = [np.pi, np.e, np.sqrt(2), np.sqrt(7)]

fig, ((p1, p2), (p3, p4)) = plt.subplots(2, 2)
plots = [p1, p2, p3, p4]

for i, r in enumerate(ratio):
    f_x = f_y * r
    results = trig_np(f_x, f_y, a_x, a_y, phi, dt, n)
    plots[i].plot(results[1], results[0])

p1.set_title('ratio = $\pi$')
p2.set_title('ratio = e')
p3.set_title('ratio = $\sqrt{2}$')
p4.set_title('ratio = $\sqrt{7}$')

p3.set_xlabel('$Y(t)$') 
p4.set_xlabel('$Y(t)$')

p1.set_ylabel('$X(t)$')
p3.set_ylabel('$X(t)$') 
 
plt.suptitle('$f_x/f_y$ Irrational')

plt.tight_layout()
plt.show()
