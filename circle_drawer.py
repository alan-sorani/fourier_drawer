from itertools import count
import matplotlib
matplotlib.rcParams['figure.figsize'] = [10, 10]
import matplotlib.pyplot as plt
plt.switch_backend('QT4Agg')
import math, cmath
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

arrow_color = '#ffffff'
trace_color = '#ffdd00'
background_color = '#000033'
circle_color = arrow_color

canvas_size = 4
speed = 1 
increment = 1/100
coefficients = [complex(0), complex(1), complex(0), complex(0), complex(0), complex(0.5), complex(0), complex(0), complex(0), complex(0), complex(0.7)]

ax=plt.axes()
ax.set_facecolor(background_color)
index = count()
x_vals = []
y_vals = []
trace = [[],[]]

def plot_graph(coefficients):
    positions, angles = zip(*[cmath.polar(z) for z in coefficients])

def update_points():
    t = next(index)
    
    x = [coefficients[0].real]
    y = [coefficients[0].imag]
    
    for k in range(1, len(coefficients)):
        r, theta = cmath.polar(coefficients[k])
        x.append(x[-1] + r * math.cos(theta + k * increment * t))
        y.append(y[-1] + r * math.sin(theta + k * increment * t))
    trace[0].append(x[-1])
    trace[1].append(y[-1])
    return x, y

def draw_arrows(x,y):
    for i in range(1, len(x)):
        dx = x[i] - x[i-1]
        dy = y[i] - y[i-1]
        radius = math.sqrt(dx**2 + dy**2)
        plt.arrow(x[i-1], y[i-1], 0.85*dx, 0.85*dy, color = arrow_color, width = radius * 0.005, head_width = radius * 0.1, overhang=-0.2)
        circ = plt.Circle((x[i-1], y[i-1]), radius, fill=False, color=circle_color, linewidth = radius * 0.5)
        plt.gca().add_patch(circ)

def animate(i):
    plt.cla()

    for i in range(speed):
        x_vals, y_vals = update_points()
    
    plt.cla()
    draw_arrows(x_vals, y_vals)
    plt.plot(trace[0], trace[1], color = trace_color)
    plt.xlim(-canvas_size/2, canvas_size/2)
    plt.ylim(-canvas_size/2, canvas_size/2)
    plt.autoscale(False)

ani = FuncAnimation(plt.gcf(), animate, interval=1)
plt.tight_layout()
plt.axis('scaled')

plt.show()
