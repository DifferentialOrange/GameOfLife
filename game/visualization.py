import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def PlotGridRaw(field, shape):
	im = plt.imshow(field, cmap='Greys')

	ax = plt.gca()

	ax.set_xticks(np.arange(0, shape[0], 1))
	ax.set_yticks(np.arange(0, shape[0], 1))

	ax.set_xticklabels(np.arange(1, shape[0] + 1, 1))
	ax.set_yticklabels(np.arange(1, shape[0] + 1, 1))

	ax.set_xticks(np.arange(-.5, shape[0], 1), minor=True)
	ax.set_yticks(np.arange(-.5, shape[0], 1), minor=True)

	ax.grid(which='minor', color='grey', linestyle='-', linewidth=2)

	for axi in (ax.xaxis, ax.yaxis):
		for tic in axi.get_major_ticks():
			tic.tick1line.set_visible(False)
			tic.tick2line.set_visible(False)
		for tic in axi.get_minor_ticks():
			tic.tick1line.set_visible(False)
			tic.tick2line.set_visible(False)
		
	ax.tick_params(axis='x', colors=(0,0,0,0))
	ax.tick_params(axis='y', colors=(0,0,0,0))

	return im

def PlotGrid(field_obj):
	field = field_obj.GetField()
	shape = field_obj.GetShape()

	return PlotGridRaw(field, shape)

def SaveAnimation(field_obj, frames=10, path='animation.gif'):
	shape = field_obj.GetShape()

	def animate(i):
		if i == 0:
			PlotGrid(field_obj)
		else:
			field_obj.NextStep()
			PlotGrid(field_obj)

	ani = animation.FuncAnimation(plt.figure(figsize=shape), animate, frames=frames, interval=400)
	ani.save(path, writer='imagemagick');

	return ani
