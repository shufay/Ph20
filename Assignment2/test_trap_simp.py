'''
Evaluates the trapezoidal and Simpson's formula routines.
'''

from integrate import *

tolerance = 1/10**5

# Integral of e^x over [0,1]
e_int = np.e - 1


N = np.linspace(1, 1000, 1000)

# Trapezoidal formula
trap = np.vectorize(int_trap) 

# Error for trapezoidal formula
error_trap = abs(e_int - trap(np.exp, 0, 1, N)) 
thresh_trap = np.where(error_trap < tolerance)[0][0]
n_trap = N[thresh_trap]

# Simpson's formula
simp = np.vectorize(int_simp) 

# Error Simpson's formula
error_simp = abs(e_int - simp(np.exp, 0, 1, N)) 
thresh_simp = np.where(error_simp < tolerance)[0][0]
n_simp = N[thresh_simp]

# --------------------------------------------------------
# Plot global error for each method as a function of N
# --------------------------------------------------------

e_t = np.vectorize(e_trap)
e_s = np.vectorize(e_simp)
et = e_t(0, 1, N)
es = e_s(0, 1, N)
thresh_t = np.where(et < tolerance)[0][0]
thresh_s = np.where(es < tolerance)[0][0]
n_t = N[thresh_t]
n_s = N[thresh_s]

fig, (errt, errs) = plt.subplots(1, 2)
errt.plot(N, et)
errt.set_xlabel('N')
errt.set_ylabel('Global Error, Trapezoidal')
errt.axvline(x=n_t, color='black', linestyle='--')
errt.text(n_t+20, 0.13, f'N ={n_t}')

errs.plot(N, es)
errs.set_xlabel('N')
errs.set_ylabel("Global Error, Simpson's")
errs.axvline(x=n_s, color='black', linestyle='--')
errs.text(n_s+20, 0.00055, f'N ={n_s}')

plt.tight_layout()


# --------------------------------------------------------
# Plot errors for the integration routines written as a 
# function of N
# --------------------------------------------------------
fig, (ptrap, psimp) = plt.subplots(1, 2)
ptrap.plot(N, error_trap)
ptrap.set_xlabel('N')
ptrap.set_ylabel('Error, |$I - I_\mathrm{trap}$|')
ptrap.axvline(x=n_trap, color='black', linestyle='--')
ptrap.text(n_trap+20, 0.13, f'N ={n_trap}')

psimp.plot(N, error_simp)
psimp.set_xlabel('N')
psimp.set_ylabel('Error, |$I - I_\mathrm{simp}$|')
psimp.axvline(x=n_simp, color='black', linestyle='--')
psimp.text(n_simp+20, 0.00055, f'N ={n_simp}')

plt.tight_layout()

fig2, (ptrap_pow, psimp_pow) = plt.subplots(1, 2)
ptrap_pow.plot(1/N**(2), error_trap)
ptrap_pow.set_xlabel('$N^{-2}$')
ptrap_pow.set_ylabel('Error, |$I - I_\mathrm{trap}$|')

psimp_pow.plot(1/N**(4), error_simp)
psimp_pow.set_xlabel('$N^{-4}$')
psimp_pow.set_ylabel('Error, |$I - I_\mathrm{simp}$|')

plt.tight_layout()
plt.show()

