'''
Evaluates the general routine.
'''

from integrate import *

# Integral of e^x over [0,1]
e_int = np.e - 1

# Evaluate using the general integration function
N = 100
gen1 = int_gen(np.exp, 0, 1, N, 1/10**(9))
gen2 = int_gen(np.exp, 0, 1, N, 1/10**(14))

trap = int_trap(np.exp, 0, 1, N)
errt = abs(e_int - trap)

simp = int_simp(np.exp, 0, 1, N)
errs = abs(e_int - simp)

print('Function = e^x')
print('Value = ', e_int)

print('\nGeneral Method')
print('Input N = ', N)
print('relative accuracy = 10^(-9)')
print('value =  ', gen1[0])
print('iterations =  ', gen1[1])

print('\nrelative accuracy = 10^(-14)')
print('value =  ', gen2[0])
print('iterations =  ', gen2[1])

print('\nTrapezoidal Formula')
print('N = ', N)
print('int = ', trap)
print('error = ', errt)

print("\nSimpson's Formula")
print('N = ', N)
print('int = ', simp)
print('error = ', errs)

# Evaluate integral of tan(x) over [0, pi/4]
cos = int_gen(np.cos, 0, np.pi/4, N, 1/10**(14))
errc = abs(np.sin(np.pi/4) - cos[0])

print('\nFunction = cos(x)')
print('value = ', np.sin(np.pi/4))
print('\nrelative accuracy = 10^(-14)')
print('value = ', cos[0])
print('iterations = ', cos[1])
print('error = ', errc)
