'''
Evaluate with scipy.integrate.quad and scipy.integrate.romberg.
'''

import scipy.integrate as it
import numpy as np
from integrate import *

# Integral of e^x over [0,1]
e_int = np.e - 1

quad = it.quad(lambda x: np.exp(x), 0, 1)[0]
romb = it.romberg(lambda x: np.exp(x), 0, 1)
trap = int_trap(np.exp, 0, 1, 1000)
simp = int_simp(np.exp, 0, 1, 1000)

e_quad = abs(e_int - quad)
e_romb = abs(e_int - romb)
e_trap = abs(e_int - trap)
e_simp = abs(e_int - simp)

print('value: ', e_int)

print("\nquad: ", quad)
print('error: ', e_quad)

print("\nromberg: ", romb)
print('error: ', e_romb)

print('\ntrapezoidal: ', trap)
print('error: ', e_trap)

print("\nsimpson's: ", simp)
print('error: ', e_simp)
