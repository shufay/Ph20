import numpy as np
import matplotlib.pyplot as plt

def x_anal(t):
	return 3 * np.cos(t)

def v_anal(t):
	return -3 * np.sin(t)

def spring_im(x0, v0, h, N):
	t = np.linspace(0, h*N, N)
	x = np.zeros(N)
	v = np.zeros(N)
	x[0] = x0
	v[0] = v0

	for i in range(1, N):
		x[i] = (x0 + h * v0) / (1 + h**2)
		v[i] = (v0 - h * x0) / (1 + h**2)
		x0 = x[i]
		v0 = v[i]

	return t, x, v

def spring_ex(x0, v0, h, N):
	t = np.linspace(0, h*N, N)
	x = np.zeros(N)
	v = np.zeros(N)
	x[0] = x0
	v[0] = v0

	for i in range(1, N):
		x[i] = x0 + h * v0
		v[i] = v0 - h * x0
		x0 = x[i]
		v0 = v[i]

	return t, x, v

def symplectic(x0, v0, h, N):
    t = np.linspace(0, h*N, N)
    x = np.zeros(N)
    v = np.zeros(N)
    x[0] = x0
    v[0] = v0

    for i in range(1, N):
        x[i] = x0 + h * v0
        v[i] = v0 - h * x[i]
        x0 = x[i]
        v0 = v[i]

    return t, x, v

def energy_sym(x0, v0, h0, N):
    sym = symplectic(x0, v0, h0, N)
    return sym[0], np.square(sym[1]) + np.square(sym[2])

# Constants
x0 = 2
v0 = 5
h0 = 0.01
N = 5000

# Spring (explicit)
spring_x = spring_ex(x0, v0, h0, N)

# Spring (implicit)
spring_m = spring_im(x0, v0, h0, N)

# Spring (symplectic)
spring_sym = symplectic(x0, v0, h0, N)

# Spring (analytic)
spring_anx = x_anal(spring_x[0])
spring_anv = v_anal(spring_x[0])

# Energy (symplectic)
energy = energy_sym(x0, v0, h0, N)

# Global error
h0 = 0.1
N = 50000

error_sym = symplectic(x0, v0, h0, N)
error_x = x_anal(error_sym[0])

# Plot
# Phase space 
fig, ((an, sym), (ex, im)) = plt.subplots(2, 2)

# Spring (analytical)
an.plot(spring_anx, spring_anv)
an.set_xlabel('x (m)')
an.set_ylabel('v (m/s)')
an.set_title('Analytical')

# Spring (symplectic)
sym.plot(spring_sym[1], spring_sym[2])
sym.set_xlabel('x (m)')
sym.set_ylabel('v (m/s)')
sym.set_title('Symplectic')

# Spring (explicit)
ex.plot(spring_x[1], spring_x[2])
ex.set_xlabel('x (m)')
ex.set_ylabel('v (m/s)')
ex.set_title('Explicit Euler Method')

# # Spring (implicit)
im.plot(spring_m[1], spring_m[2])
im.set_xlabel('x (m)')
im.set_ylabel('v (m/s)')
im.set_title('Implicit Euler Method')

plt.tight_layout()

# Symplectic spring
fig2, (sym_x, sym_v) = plt.subplots(1, 2)

sym_x.plot(spring_sym[0], spring_sym[1])
sym_x.set_xlabel('t (s)')
sym_x.set_ylabel('x (m)')

sym_v.plot(spring_sym[0], spring_sym[2])
sym_v.set_xlabel('t (s)')
sym_v.set_ylabel('v (m/s)')

plt.tight_layout()

# Energy of symplectic spring
plt.figure()
plt.plot(energy[0], energy[1])
plt.xlabel('t (s)')
plt.ylabel('E (J)')

# Global error
plt.figure()
err_sym, = plt.plot(error_sym[0][N-400:], error_sym[1][N-400:], label='Symplectic')
err_an, = plt.plot(error_sym[0][N-400:], error_x[N-400:], label='Analytical')
plt.legend(handles=[err_sym, err_an])
plt.xlabel('t (s)')
plt.ylabel('x (m)')

plt.show()