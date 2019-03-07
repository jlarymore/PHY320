# Author: Larry Engelhardt (July, 2016)

from pylab import *

## YOU WILL NEED TO ADD AND CHANGE CODE BELOW ##

Nx = 0                # Number of positions in space
x = linspace(0, 0, 0) # Array of positions
dx  = 0               # Size of one slice of space
Nt = 0                # Number of time steps
t = linspace(0, 0, 0) # Array of time values
dt  = 0               # Size of time step


# Preparing 2D array of temperatures
T = zeros((Nt, Nx)) # 2D array for temperature. NOTE THE ORDER: [time, space]

## Example showing how to create a plot
y = sin(x)
plot(x, y, linewidth=2)
grid(True)
xlabel('x axis label')
ylabel('y axis label')
savefig('An Empty Plot.png')
grid(True); show()


## Structure of the loop that you will need to use
## to compute the temperature of the handle for all x & t:

for j in range(1, Nt):
    for i in range(1, Nx-1):
        T[j,i] = 0
    T[j, -1] = 0


# Example of how to create a contour plot
# Note, the following code will probably produce an error
# if you try to execute it before you modify the code above.
# This is because the arrays x, t, and T are initially set to have zero elements.

colorvals = linspace(70, 160, 91) # Colors for the contour plot (min, max, num)
contourf(x, t, T, colorvals)      # (x-axis, y-axis, z(x,y))
title('An Empty Contour Plot')
xlabel('x axis label')
ylabel('y axis label')
colorbar()
grid(True);  show()

