import numpy as np
g = 9.81
c = 0.05
l =10.

delta_time = 0.1
time_start = 0.0
time_end = 10.0

previous_theta = (1*np.pi)/180.
previous_angvel = 0.

theta_list = []
ang_vel_list = []

for i in range(500):
    ang_vel = -(g/l)*previous_theta*delta_time -c*previous_angvel + previous_angvel
    new_theta = previous_theta + previous_angvel*delta_time

    theta_list.append(new_theta)
    ang_vel_list.append(ang_vel)

    previous_angvel = ang_vel
    previous_theta = new_theta

import matplotlib.pyplot as plt
plt.plot(range(len(theta_list)),theta_list)
plt.show()
