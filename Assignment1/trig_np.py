# #!/usr/bin/python
import sys
import matplotlib.pyplot as plt
import numpy as np

def X(f_x, a_x, t):
    return a_x * np.cos(2 * np.pi * f_x * t)

def Y(f_y, a_y, t, phi):
    return a_y * np.sin(2 * np.pi * f_y * t + phi)

def Z(X, Y):
    return X + Y

def trig_np(f_x, f_y, a_x, a_y, phi, dt, n):
    '''
    Computes trigonometric functions X(t), Y(t) and Z(t). Stores the 
    results in numpy arrays. Outputs the results to .txt files 
    "X_np_out.txt", "Y_np_out.txt" and "X_np_out.txt".
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

def write_file(f_x, f_y, a_x, a_y, phi, dt, n):
    '''
    Writes the results to 3 files.
    '''
    results = trig_np(f_x, f_y, a_x, a_y, phi, dt, n)

    fileX = open('X_np_out.txt', 'w')
    fileY = open('Y_np_out.txt', 'w')
    fileZ = open('Z_np_out.txt', 'w')

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