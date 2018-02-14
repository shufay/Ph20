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

def spring_trunc(x0, v0, h, N):
	sp = spring_ex(x0, v0, h, N)
	return np.amax(x_anal(sp[0]) - sp[1])

def energy_ex(x0, v0, h, N):
	sp = spring_ex(x0, v0, h, N)
	return sp[0], np.square(sp[1]) + np.square(sp[2])

def energy_im(x0, v0, h, N):
	sm = spring_im(x0, v0, h, N)
	return sm[0], np.square(sm[1]) + np.square(sm[2])

# Constants
x0 = 3
v0 = 0
h0 = 0.001
N = 30000

# Spring (explicit)
spring_x = spring_ex(x0, v0, h0, N)

# Energy (explicit)
enx = energy_ex(x0, v0, h0, N)
# long range trend: increases linearly 
# follows linear trend in error

# Spring (implicit)
spring_m = spring_im(x0, v0, h0, N)

# Energy (implicit)
enm = energy_im(x0, v0, h0, N)

# Global Error (explicit)
xerr_x = x_anal(spring_x[0]) - spring_x[1]
verr_x = v_anal(spring_x[0]) - spring_x[2]

# Global Error (implicit)
xerr_m = x_anal(spring_m[0]) - spring_m[1]
verr_m = v_anal(spring_m[0]) - spring_m[2]

# Truncation error
h = np.array([1., 0.5, 0.25, 0.125, 0.0625])
h1 = 1/h
h1 = h1.astype(np.int64)
spring_t = np.zeros(5)

for i, item in enumerate(h):
	spring_t[i] = spring_trunc(x0, v0, h0 * item, N * h1[i])

# Plot
# Explicit Euler method
fig, (x_ex, v_ex) = plt.subplots(1, 2)

x_ex.plot(spring_x[0], spring_x[1])
x_ex.set_xlabel('t (s)')
x_ex.set_ylabel('x (m)')

v_ex.plot(spring_x[0], spring_x[2])
v_ex.set_xlabel('t (s)')
v_ex.set_ylabel('v (m/s)')

plt.suptitle('Explicit Euler Method')
plt.tight_layout()

# Global error (explicit)
fig2, (xerror_x, verror_x) = plt.subplots(1, 2)

xerror_x.plot(spring_x[0], xerr_x)
xerror_x.set_xlabel('t (s)')
xerror_x.set_ylabel('$x_\mathrm{error}$')

verror_x.plot(spring_x[0], verr_x)
verror_x.set_xlabel('t (s)')
verror_x.set_ylabel('$v_\mathrm{error}$')

plt.suptitle('Explicit Euler Method')
plt.tight_layout()

# Global error (implicit)
fig3, (xerror_m, verror_m) = plt.subplots(1, 2)

xerror_m.plot(spring_m[0], xerr_m)
xerror_m.set_xlabel('t (s)')
xerror_m.set_ylabel('$x_\mathrm{error}$')

verror_m.plot(spring_m[0], verr_m)
verror_m.set_xlabel('t (s)')
verror_m.set_ylabel('$v_\mathrm{error}$')

plt.suptitle('Implicit Euler Method')
plt.tight_layout()

# Implicit Euler method
fig4, (x_im, v_im) = plt.subplots(1, 2)

x_im.plot(spring_m[0], spring_m[1])
x_im.set_xlabel('t (s)')
x_im.set_ylabel('x (m)')

v_im.plot(spring_m[0], spring_m[2])
v_im.set_xlabel('t (s)')
v_im.set_ylabel('v (m/s)')

plt.suptitle('Implicit Euler Method')
plt.tight_layout()

# Max x_error
plt.figure()
plt.plot(h, spring_t)
plt.xlabel('$h/h_0$')
plt.ylabel('Maximum $x_\mathrm{error}$')

# Energy (explicit)
plt.figure()
plt.plot(enx[0], enx[1])
plt.xlabel('t (s)')
plt.ylabel('$\mathrm{Energy_{explicit}}$ (J)')

# Energy (implicit)
plt.figure()
plt.plot(enm[0], enm[1])
plt.xlabel('t (s)')
plt.ylabel('$\mathrm{Energy_{implicit}}$ (J)')

plt.show()
