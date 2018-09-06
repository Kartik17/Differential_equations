import numpy as np
g = 9.81
c = 0.005
l =10.
m= 1.

delta_time = 0.1
time_start = 0.0
time_end = 10.0

theta_list = [(1*np.pi)/180.]
ang_vel_list = [0.]


for i in range(500):
    ang_vel_der = -(g/l)*theta_list[-1] -(c/m*l*l)*ang_vel_list[-1]

    ang_vel_current = (ang_vel_der)*delta_time + ang_vel_list[-1]
    theta_current = theta_list[-1] + ang_vel_list[-1]*delta_time

    theta_list.append(theta_current)
    ang_vel_list.append(ang_vel_current)


import matplotlib.pyplot as plt
plt.plot(range(len(ang_vel_list)),theta_list)
plt.show()
