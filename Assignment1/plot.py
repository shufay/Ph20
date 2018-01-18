# #!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

'''
Plots the graph of X(t) against Y(t) from calling trig_lists.py
'''
# Read files
X_out = open('X_np_out.txt', 'r')
Y_out = open('Y_np_out.txt', 'r')

X = np.array([])
Y = np.array([])

for x in X_out:
    X = np.append(X, np.array(float(x)))

for y in Y_out:
    Y = np.append(Y, np.array(float(y)))

X_out.close()
Y_out.close()

# Plot
plt.plot(Y, X)
plt.xlabel('$Y(t)$')
plt.ylabel('$X(t)$')
plt.show()


