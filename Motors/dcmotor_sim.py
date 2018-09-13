import numpy as np
import matplotlib.pyplot as plt

V = 24
R = 10
L = 0.24
b = 0.000001
kb = 0.02
kt = 0.02
I = 9e-6
delta_t = 0.001

T_load = [0., 0.001,0.01, 0.05, 0.1]
stall_torque = kt*(V/R)

i_phase = [0.]
w = [0.]
theta = [0.]
i_constant =[]
w_constant = []
print(stall_torque, V/kb)

print('Time Constant: {:2f}'.format(L/R))
for load in T_load:
    i_phase = [0.]
    w = [0.]
    theta = [0.]
    for i in range(1,500000):
        i_phase.append((delta_t/L)*(V - i_phase[i-1]*R - kb*w[i-1]) + i_phase[i-1])
        if i_phase[i]>=2.4:
            i_phase = 2.4
        elif i_phase[i]<=0:
            i_phase[i] = 0.
        w.append((delta_t/I)*(kt*i_phase[i-1] - load - b*w[i-1]) + w[i-1])
        if w[i] <=0:
            w[i] = 0.
        elif w[i] >= 1200:
            w[i] = 1200.0
        theta.append((delta_t)*w[i-1] +theta[i-1])

    print(i_phase[-1], V/R)
    print(w[-1])
    i_constant.append(kt*i_phase[-1])
    w_constant.append(w[-1])
plt.plot(i_constant,w_constant)
plt.ylim([0,1200])
plt.xlim([0,0.05])
plt.show()
