import numpy as np
import matplotlib.pyplot as plt

def lin(x):
	return x**2

def int_trap(func, a, b, N):
	'''
	Integrates a function 'func' over [a,b] using the extended 
	trapezoidal formula. The interval [a,b] is divided into N partitions.
	'''
	dx = (b-a)/N
	x = np.linspace(a, b, N+1)
	y = func(x)
	y[0] /= 2
	y[-1] /= 2
	integral = np.sum(dx * y)
	return integral

def int_simp(func, a, b, N):
	'''
	Integrates a function 'func' over [a,b] using the extended 
	Simpson's formula. The interval [a,b] is divided into N partitions.
	'''
	dx = (b-a)/N
	mid = np.linspace(a+dx/2, b-dx/2, N) # midpoints in intervals
	x = np.linspace(a, b, N+1) # endpoints of intervals
	y_x = func(x)
	y_mid = func(mid) 
	y_x[0] /= 2
	y_x[-1] /= 2
	integral = (dx/3) * (np.sum(y_x) + np.sum(2 * y_mid))
	return integral

def int_gen(func, a, b, N, acc):
	'''
	General-purpose integration function that evaluates an integral with 
	Simpson's formula to a desired level of relative accuracy 'acc'. N 
	is the base number of subintervals to divide the interval [a,b] into.
	'''
	k = 0
	I_simp1 = int_simp(func, a, b, 2** k * N)
	I_simp2 = int_simp(func, a, b, 2**(k+1) * N)
	diff = abs((I_simp1 - I_simp2) / I_simp1)

	while diff > acc:
		k += 1
		I_simp1 = int_simp(func, a, b, 2** k * N)
		I_simp2 = int_simp(func, a, b, 2**(k+1) * N)
		diff = abs((I_simp1 - I_simp2) / I_simp1)

	return I_simp2, k+1

def e_trap(a, b, N):
	return np.e**(0.5) * (b-a)/12 * ((b-a)/N)**2

def e_simp(a, b, N):
	return np.e**(0.5) * (b-a)/2880 * ((b-a)/N)**4
