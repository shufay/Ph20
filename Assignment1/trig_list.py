# #!/usr/bin/python

import math, sys
import matplotlib.pyplot as plt

def X(f_x, a_x, t):
    return a_x * math.cos(2 * math.pi * f_x * t)

def Y(f_y, a_y, t, phi):
    return a_y * math.sin(2 * math.pi * f_y * t + phi)

def Z(X, Y):
    return X + Y

def trig_list(f_x, f_y, a_x, a_y, phi, dt, n):
    '''
    Computes trigonometric functions X(t), Y(t) and Z(t). Stores the 
    results in python lists. Outputs the results to .txt files 
    "X_list_out.txt", "Y_list_out.txt" and "X_list_out.txt".
    '''
    t = dt * np.arange(0, n+1)

    X_out = X(f_x, a_x, t)
    Y_out = Y(f_y, a_y, t, phi)
    Z_out = Z(X_out, Y_out)

    return X_out, Y_out, Z_out

def write_file(f_x, f_y, a_x, a_y, phi, dt, n):
    '''
    Writes the results to 3 files.
    '''
    results = trig_list(f_x, f_y, a_x, a_y, phi, dt, n)

    fileX = open('X_list_out.txt', 'w')
    fileY = open('Y_list_out.txt', 'w')
    fileZ = open('Z_list_out.txt', 'w')

    for i in range(n + 1):
        fileX.write(str(results[0][i]) + '\n')
        fileY.write(str(results[1][i]) + '\n')
        fileZ.write(str(results[2][i]) + '\n')
        
    fileX.close()
    fileY.close()
    fileZ.close()

# Run program
# arguments: f_x f_y a_x a_y phi dt n

if len(sys.argv) != 8:
    usage = 'arguments: f_x f_y a_x a_y phi dt n'
    print(usage)
    
fx_in = float(sys.argv[1])
fy_in = float(sys.argv[2])
ax_in = float(sys.argv[3])
ay_in = float(sys.argv[4])
phi_in = float(sys.argv[5])
dt_in = float(sys.argv[6])
n_in = int(sys.argv[7])

write_file(fx_in, fy_in, ax_in, ay_in, phi_in, dt_in, n_in)