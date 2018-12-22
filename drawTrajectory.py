# -*- coding: utf-8 -*-


import readtxt 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = '/home/xdh/rays.txt'

rays = readtxt.readtxt(filename, ' ')

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax = plt.subplot('111', projection='3d')

#plt.plot(rays[:,0], rays[:,1], rays[:,2])
#plt.plot(rays[:,0], rays[:,1])


fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(rays[:,0], rays[:,1], rays[:,2])


plt.show()


