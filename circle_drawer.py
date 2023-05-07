from itertools import count
import matplotlib
matplotlib.rcParams['figure.figsize'] = [10, 10]
import matplotlib.pyplot as plt
plt.switch_backend('QT4Agg')
import math, cmath
from matplotlib.animation import FuncAnimation
import numpy as np
from functools import partial

speed = 1 
increment = 1/100

def order_coefficients(coefficients):
    return dict(sorted(coefficients.items(),
                       key=lambda item: np.abs(item[1]), reverse=True))

def determine_size(coefficients, margin):
    radius_sum = 0
    for i in coefficients:
        radius_sum = radius_sum + np.abs(coefficients[i])
    return 2 * (radius_sum + margin)

def plot_graph(coefficients):
    positions, angles = zip(*[cmath.polar(z) for z in coefficients])

def update_points(coefficients, index, trace):
    t = next(index)
    
    x = [coefficients[0].real]
    y = [coefficients[0].imag]
    
    for i in coefficients:
        r, theta = cmath.polar(coefficients[i])
        x.append(x[-1] + r * math.cos(theta + i * increment * t))
        y.append(y[-1] + r * math.sin(theta + i * increment * t))
    trace[0].append(x[-1])
    trace[1].append(y[-1])
    return x, y

def draw_arrows(x,y,arrow_color,circle_color):
    for i in range(1, len(x)):
        dx = x[i] - x[i-1]
        dy = y[i] - y[i-1]
        radius = math.sqrt(dx**2 + dy**2)
        plt.arrow(x[i-1], y[i-1], 0.85*dx, 0.85*dy, color = arrow_color,
                  width = radius * 0.005,
                  head_width = radius * 0.1, overhang=-0.2)
        circ = plt.Circle((x[i-1], y[i-1]), radius,
                          fill=False, color=circle_color,
                          linewidth = radius * 0.5)
        plt.gca().add_patch(circ)

def animate(i,
            coefficients, canvas_size, margin,
            arrow_color, trace_color, circle_color, index, trace):
    plt.cla()

    for i in range(speed):
        x_vals, y_vals = update_points(coefficients, index, trace)
    
    plt.cla()
    draw_arrows(x_vals,y_vals,arrow_color,circle_color)
    plt.plot(trace[0], trace[1], color = trace_color)
    plt.xlim(-canvas_size/2, canvas_size/2)
    plt.ylim(-canvas_size/2, canvas_size/2)
    plt.autoscale(False)

def circle_drawer(coefficients, ordering = True, margin = 0.1,
                   arrow_color = '#ffffff', trace_color = '#ffdd00',
                  background_color = '#000033', circle_color = None):
    ax=plt.axes()
    ax.set_facecolor(background_color)
    canvas_size = determine_size(coefficients, margin)
    if(ordering == True):
        coefficients = order_coefficients(coefficients)
    if circle_color is None:
        circle_color = arrow_color
    
    index = count()
    trace = [[],[]]
    
    ani = FuncAnimation(plt.gcf(), partial(animate,
                                           coefficients=coefficients,
                                           canvas_size=canvas_size,
                                           margin=margin,
                                           arrow_color=arrow_color,
                                           trace_color=trace_color,
                                           circle_color=circle_color,
                                           index=index,
                                           trace=trace),
                        interval=1)
    plt.tight_layout()
    plt.axis('scaled')

    plt.show()
