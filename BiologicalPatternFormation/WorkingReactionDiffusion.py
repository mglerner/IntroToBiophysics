#!/usr/bin/env python
# coding: utf-8

# > This is one of the 100 recipes of the [IPython Cookbook](http://ipython-books.github.io/), the definitive guide to high-performance scientific computing and data science in Python.
# 

# Links:
# 
#  * http://mrob.com/pub/comp/xmorphia/F260/F260-k550.html
#  * http://mrob.com/pub/comp/xmorphia/

# # 12.4. Simulating a Partial Differential Equation: reaction-diffusion systems and Turing patterns

# 1. Let's import the packages.

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


Du = 0.00016
Dv = 0.00008
F= 0.0350  
k= 0.065

colormap = plt.cm.copper
colormap = plt.cm.jet

size = 100  # size of the 2D grid
dx = 2./size  # space step

T = 100.0  # total time
dt = .9 * dx**2/2  # time step
n = int(T/dt)
steps_per_frame = 1000
print "We will show {n} steps, {s} steps per frame".format(n=n,s=steps_per_frame)
n = int(n/steps_per_frame)


# Make life nicer for setting up our initial conditions
def makeblock(data,xcenter,xhalflength,ycenter,yhalflength,value=1):
    data[xcenter-xhalflength:xcenter+xhalflength,ycenter-yhalflength:ycenter+yhalflength] = value

if size == 100:
    U = np.zeros((size,size))
    V = np.zeros((size,size))
    if 0:
        makeblock(U,15,5,15,5)
        makeblock(V,16,5,16,5)

        makeblock(U,15,5,30,5)
        makeblock(V,16,5,32,5)
    elif 0:
        makeblock(U,15,5,15,5)
        makeblock(U,15,5,30,5)
    elif 0:
        U = np.random.rand(size, size)
        V = np.random.rand(size, size)
    elif 0:
        makeblock(U,15,5,15,5,0.2)
        makeblock(V,16,5,16,5,0.1)
        makeblock(V,15,5,15,5)
        makeblock(V,15,5,30,5)
    else:
        for i in range(20):
            x,y = np.random.randint(0,size,2)
            makeblock(U,x,5,y,5)
            makeblock(V,x,5,y,5)
        
else:
    U = np.random.rand(size, size)
    V = np.random.rand(size, size)

def laplacian(Z):
    Ztop = Z[0:-2,1:-1]
    Zleft = Z[1:-1,0:-2]
    Zbottom = Z[2:,1:-1]
    Zright = Z[1:-1,2:]
    Zcenter = Z[1:-1,1:-1]
    return (Ztop + Zleft + Zbottom + Zright - 4 * Zcenter) / dx**2


fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
im1 = plt.imshow(U,cmap=colormap,interpolation='none',vmin=0,vmax=1)
ax2 = fig.add_subplot(1,2,2)
im2 = plt.imshow(V,cmap=colormap,interpolation='none',vmin=0,vmax=1)
#ax = plt.axes(xlim=(0,size),ylim=(0,size))
bbox_props = dict(boxstyle="Round,pad=0.3", fc="cyan", ec="b", lw=2)
description_text = ax1.text(size-40, size-10, "Direction", ha="center", va="center",# rotation=45,
            size=15,
            bbox=bbox_props)



#description_text = ax.text(5,5,'cows')

def init():
    #plt.imshow(U,cmap=colormap,interpolation='none')
    description_text.set_text('frogs')
    cbar_ax = fig.add_axes([0.90, 0.15, 0.025, 0.7])
    fig.colorbar(im1, cax=cbar_ax)
    return [im1,im2,description_text]


# In[79]:

# We simulate the PDE with the finite difference method.
def animate(i):
    # We compute the Laplacian of u and v.
    for ii in range(steps_per_frame):
        deltaU = laplacian(U)
        deltaV = laplacian(V)
        # We take the values of u and v inside the grid.
        Uc = U[1:-1,1:-1]
        Vc = V[1:-1,1:-1]
        # We update the variables.
        U[1:-1,1:-1] = Uc + dt * (Du * deltaU - Uc*Vc*Vc + F*(1-Uc))
        V[1:-1,1:-1] = Vc + dt * (Dv * deltaV + Uc*Vc*Vc - (F+k)*Vc)
        # Neumann conditions: derivatives at the edges
        # are null.
        for Z in (U, V):
            Z[0,:] = Z[1,:]
            Z[-1,:] = Z[-2,:]
            Z[:,0] = Z[:,1]
            Z[:,-1] = Z[:,-2]
    im1.set_array(U)
    im2.set_array(V)
    description_text.set_text('F {F} k {k} i {i}'.format(F=F,k=k,i=i))
    return [im1,im2,description_text]

anim = animation.FuncAnimation(fig, animate, init_func=init, repeat=False,
                               frames=n, interval=20,
                               #blit=True
                               )

plt.show()
