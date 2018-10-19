import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def init():
	line.set_data([],[])
	return line,

def animate(i):
	global x,y
	line.set_data(x[:i],y[:i])
	return line,


if __name__ == '__main__':
	t_min = 0.
	t_max = 24*np.pi
	dt = 0.02
	t = np.arange(t_min,t_max,dt)
	x,y = [],[]

	for i in range(len(t)):
		x.append(np.sin(t[i])*(np.exp(np.cos(t[i])) -2*np.cos(4*t[i]) - (np.sin(t[i]/12.))**5 ))
		y.append(np.cos(t[i])*(np.exp(np.cos(t[i])) -2*np.cos(4*t[i]) - (np.sin(t[i]/12.))**5 ))

	fig = plt.figure()
	ax = fig.add_subplot(111, aspect = 'equal', autoscale_on = False, xlim = (-5,5), ylim = (-5,5))
	ax.grid()
	ax.set_xlabel('X axis')
	ax.set_ylabel('Y axis')
	line, = ax.plot([], [], '-', lw=1, c = 'g')

	anim = animation.FuncAnimation(fig, animate, init_func = init, frames = len(t), interval = 20 , blit =True)
	plt.show()
