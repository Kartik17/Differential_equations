import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation

# Constants

L1, L2 = 1, 1
m1, m2 = 1, 1
g = 9.81

# Dynamics Function -------------------------------------------------------------------------------------------------
'''
args:

y - state [theta1, omega1, theta2, omega2]
t - time 

return
dState

'''

def dynamics(y, t, L1, L2, m1, m2):
	theta1, z1, theta2, z2 = y
	c, s = np.cos(theta1-theta2), np.sin(theta1-theta2)
	theta1dot = z1
	z1dot = (m2*g*np.sin(theta2)*c - m2*s*(L1*z1**2*c + L2*z2**2) - (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*s**2)
	theta2dot = z2
	z2dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) + m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)


	return theta1dot, z1dot, theta2dot, z2dot

# Position Function -------------------------------------------------------------------------------------------------
'''
args:
y - state [theta1, omega1, theta2, omega2]

return
x1,y1,y1,y2 - Position of the Pendulum 

'''

def position(y):

	theta1 = y[:,0]
	theta2 = y[:,2]

	x1 = L1*np.sin(theta1)
	y1 = -L1*np.cos(theta1)

	x2 = L1*np.sin(theta1) + L2*np.sin(theta2)
	y2 = -L1*np.cos(theta1) - L2*np.cos(theta2)

	return x1,y1,x2,y2


# init and animate func -------------------------------------------------------------------------------------------------

def init():
	line.set_data([],[])
	return line,

def animate(i):
	global x1,x2,y1,y2
	line.set_data([0,x1[i],x2[i]],[0,y1[i],y2[i]])
	return line,

# init and animate func -------------------------------------------------------------------------------------------------

def init1():
	line1.set_data([],[])
	return line1,

def animate1(i):
	global x1,x2,y1,y2,t
	line1.set_data(x1[i:i+15],x2[i:i+15])
	return line1,


# main func -------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	
	fig = plt.figure()
	ax = fig.add_subplot(121, aspect='equal', autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
	ax.grid()
	line, = ax.plot([], [], 'o-', lw=2, c = 'r')

	ax1 = fig.add_subplot(122, aspect='equal', autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
	ax1.grid()
	line1, = ax1.plot([], [], 'o-', lw=2, c = 'b')


	total_time = 200.0
	dt = 0.02
	t  = np.arange(0., total_time, dt)
	y0 = np.array([3*np.pi/7, 10, 3*np.pi/4, 0])

	# odeint(dynamics func, initial condition of State, time, argument)
	y = odeint(dynamics, y0, t, args = (L1, L2, m1, m2))	
	x1,y1,x2,y2 = position(y)
	print(x1[1])

	anim = animation.FuncAnimation(fig, animate, init_func=init, frames=2000, interval=20, blit=True)
	anim1 = animation.FuncAnimation(fig, animate1, init_func=init1, frames=2000, interval=20, blit=True)

	plt.show()
