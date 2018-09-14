import numpy as np

# Define Constants
V = 24. #Volts
R = 10. # Ohms
kb = 0.02 #Volts/sec
kt = 0.02 #Nm/A
b = 0.000001 #
I = 8e-8
L = 0.005
p = 4
T_load = 0.
delta_t = 0.0001
total_time = delta_t*1000


def back_emf_a_func(theta):
    if theta <0.:
        print('Check')
        theta = theta + 2*np.pi

    if theta >= 0.0 and theta < np.pi/6.:
        return (6/np.pi)*theta
    elif theta >= np.pi/6. and theta < 5*np.pi/6.:
        return 1
    elif theta >= 5*np.pi/6. and theta < 7*np.pi/6.:
        return -(6/np.pi)*theta + 6
    elif theta >= 7*np.pi/6. and theta < 11*np.pi/6.:
        return -1
    elif theta >= 11*np.pi/6. and theta < 12*np.pi/6.:
        return (6/np.pi)*theta -12

def back_emf_b_func(theta):
    if theta <0.:
        print('Check')
        theta = theta + 2*np.pi

    if theta >= 0.0 and theta < 1*np.pi/2.:
        return -1
    elif theta >= 1*np.pi/2. and theta < 5*np.pi/6.:
        return (6/np.pi)*theta -4
    elif theta >= 5*np.pi/6. and theta < 3*np.pi/2.:
        return 1
    elif theta >= 3*np.pi/2. and theta < 11*np.pi/6.:
        return -(6/np.pi)*theta +10.
    elif theta >= 11*np.pi/6. and theta < 12*np.pi/6.:
        return -1

def back_emf_c_func(theta):
    if theta <0.:
        print('Check')
        theta = theta + 2*np.pi

    if theta >= 0.0 and theta < 1*np.pi/6.:
        return 1
    elif theta >= 1*np.pi/6. and theta < 1*np.pi/2.:
        return -(6/np.pi)*theta + 2
    elif theta >= 1.*np.pi/2. and theta < 7*np.pi/2.:
        return -1
    elif theta >= 7*np.pi/2. and theta < 3*np.pi/2.:
        return (6/np.pi)*theta - 8.
    elif theta >= 3*np.pi/2. and theta < 12*np.pi/6.:
        return 1

V_seq = {'1':[V/2.,-V/2.,0],'2':[V/2.,0.,-V/2],'3':[0.,V/2.,-V/2.],'4':[-V/2.,V/2.,0],'5':[-V/2.,0.,V/2.],'6':[0, -V/2., V/2.]}
i_phase = [[0.],[0.],[0.]]

w = [0]
back_emf_a = [0.0]
theta_m = [0.]
theta_e = [0.]
import math


print(kt*(V/R), V/kb)

for i in range(1,100):
    #Electrical Angle = P*Mechanical Angle
    theta_e_2pi = (theta_e[i-1])%(2*math.pi)
    print(theta_m[i-1])
    if theta_e_2pi >= 0.0 and theta_e_2pi < np.pi/3.:
        i_phase[0].append((delta_t/L)*(V_seq['1'][0] - R*i_phase[0][i-1] - kb*back_emf_a_func(theta_e_2pi)*w[i-1]) + i_phase[0][i-1])
        i_phase[1].append((delta_t/L)*(V_seq['1'][1] - R*i_phase[1][i-1] - kb*back_emf_b_func(theta_e_2pi)*w[i-1]) + i_phase[1][i-1])
        i_phase[2].append(0.0)
        back_emf_a.append(kb*back_emf_a_func(theta_e_2pi)*w[i-1])

    elif theta_e_2pi >= np.pi/3. and theta_e_2pi < 2*np.pi/3.:
        i_phase[0].append((delta_t/L)*(V_seq['2'][0] - R*i_phase[0][i-1] -kb*back_emf_a_func(theta_e_2pi)*w[i-1]) + i_phase[0][i-1])
        i_phase[1].append(0.0)
        i_phase[2].append((delta_t/L)*(V_seq['2'][2] - R*i_phase[2][i-1] -kb*back_emf_c_func(theta_e_2pi)*w[i-1]) + i_phase[2][i-1])
        back_emf_a.append(kb*back_emf_a_func(theta_e_2pi)*w[i-1])

    elif theta_e_2pi >= 2*np.pi/3. and theta_e_2pi < 3*np.pi/3.:
        i_phase[0].append(0.0)
        i_phase[1].append((delta_t/L)*(V_seq['3'][1] - R*i_phase[1][i-1] -kb*back_emf_b_func(theta_e_2pi)*w[i-1]) + i_phase[1][i-1])
        i_phase[2].append((delta_t/L)*(V_seq['3'][2] - R*i_phase[2][i-1] -kb*back_emf_c_func(theta_e_2pi)*w[i-1]) + i_phase[2][i-1])
        back_emf_a.append(0.)

    elif theta_e_2pi >= 3*np.pi/3. and theta_e_2pi < 4*np.pi/3.:
        i_phase[0].append((delta_t/L)*(V_seq['4'][0] - R*i_phase[0][i-1] -kb*back_emf_a_func(theta_e_2pi)*w[i-1]) + i_phase[0][i-1])
        i_phase[1].append((delta_t/L)*(V_seq['4'][1] - R*i_phase[1][i-1] -kb*back_emf_b_func(theta_e_2pi)*w[i-1]) + i_phase[1][i-1])
        i_phase[2].append(0.0)
        back_emf_a.append(kb*back_emf_a_func(theta_e_2pi)*w[i-1])

    elif theta_e_2pi >= 4*np.pi/3. and theta_e_2pi < 5*np.pi/3.:
        i_phase[0].append((delta_t/L)*(V_seq['5'][0] - R*i_phase[0][i-1] -kb*back_emf_a_func(theta_e_2pi)*w[i-1]) + i_phase[0][i-1])
        i_phase[1].append(0.0)
        i_phase[2].append((delta_t/L)*(V_seq['5'][2] - R*i_phase[2][i-1] -kb*back_emf_c_func(theta_e_2pi)*w[i-1]) + i_phase[2][i-1])
        back_emf_a.append(kb*back_emf_a_func(theta_e_2pi)*w[i-1])

    elif theta_e_2pi >= 5*np.pi/3. and theta_e_2pi < 6*np.pi/3.:
        i_phase[0].append(0.0)
        i_phase[1].append((delta_t/L)*(V_seq['6'][1] - R*i_phase[1][i-1] -kb*back_emf_b_func(theta_e_2pi)*w[i-1]) + i_phase[1][i-1])
        i_phase[2].append((delta_t/L)*(V_seq['6'][2] - R*i_phase[2][i-1] -kb*back_emf_c_func(theta_e_2pi)*w[i-1]) + i_phase[2][i-1])
        back_emf_a.append(0.)

    torque_a = (kb*i_phase[0][i-1]*back_emf_a_func(theta_e_2pi))
    torque_b = (kb*i_phase[1][i-1]*back_emf_b_func(theta_e_2pi))
    torque_c = (kb*i_phase[2][i-1]*back_emf_c_func(theta_e_2pi))

    torque = torque_a + torque_b + torque_c

    w.append((delta_t/I)*(torque -T_load -b*w[i-1]) + w[i-1])
    if w[i]<= 0:
        w[i] = 0.
    elif w[i] >= V/kb:
        w[i] = V/kb
    theta_m.append(delta_t*(w[i-1]) + theta_m[i-1])
    theta_e.append(theta_m[i]*p)
    #print(w[i])

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(range(len(back_emf_a)), back_emf_a)
plt.show()
