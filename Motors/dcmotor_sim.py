# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Functions

def check_params(V,kb,kt,R,L):
    print('No Load Response: {}'.format(V/kb))
    print('Stall Torque: {}'.format(kt*(V/R)))
    print('Time Constant: {:2f}'.format(L/R))

def dc_sim(load, N, n, delta_t, V, L, R, kb, kt, I_motor, I_load):
    i_phase = [0.]
    w = [0.]
    theta = [0.]
    theta_output = [0.]
    for i in range(1,5000):
        # Current 
        i_phase.append((delta_t/L)*(V - i_phase[i-1]*R - kb*w[i-1]) + i_phase[i-1])
        if i_phase[i]>=2.4:
            i_phase = 2.4
        elif i_phase[i]<=0:
            i_phase[i] = 0.

        # Angular Speed
        w.append((delta_t/(I_motor + I_load/(N**2))*(kt*i_phase[i-1] - load/(n*N) - b*w[i-1]) + w[i-1]))
        if w[i] <=0:
            w[i] = 0.
        elif w[i] >= 1200:
            w[i] = 1200.0

        # Angular Position    
        theta.append((delta_t)*w[i-1] +theta[i-1])
        theta_output.append(theta[i]*N)

    return i_phase, w, theta_output

def plot_graph(load, N, n, delta_t, V, L, R, kb, kt, I_motor, I_load):
    i_phase, w, theta_output = dc_sim(load, N, n, delta_t, V, L, R, kb, kt, I_motor, I_load)
    fig,ax = plt.subplots(2,2)
    ax[0,0].plot(range(len(i_phase)), i_phase)
    ax[0,0].set_xlabel('iteration')
    ax[0,0].set_ylabel('Current')

    ax[1,0].plot(range(len(w)), w)
    ax[1,0].set_xlabel('iteration')
    ax[1,0].set_ylabel('Angular Speed')

    ax[0,1].plot(range(len(theta_output)), theta_output)
    ax[0,1].set_xlabel('iteration')
    ax[0,1].set_ylabel('Angular Position')

    ax[1,1].plot(w, kt*np.array(i_phase))
    ax[1,1].set_xlabel('Angular Speed')
    ax[1,1].set_ylabel('Torque')

    plt.show()

if __name__ == '__main__':
    # Parameters
    V = 24
    R = 10
    L = 0.24
    b = 0.000001
    kb = 0.02
    kt = 0.02
    I_motor = 9e-6
    I_load = 0.
    N = 1
    n = 1
    delta_t = 0.001
    T_load = 0.

    check_params(V,kb,kt,R,L)
    plot_graph(T_load, N, n, delta_t, V, L, R, kb, kt, I_motor, I_load)
