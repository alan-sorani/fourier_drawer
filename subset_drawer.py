# finds a parametrization for a subset of the plane and uses fourier_coefficients and circle_drawer to use circles for drawing the subset

from fourier_coefficients import fourier_coefficients
from circle_drawer import circle_drawer

def draw_function(func,last_index,initial_time,final_time):
    coefficients=fourier_coefficients(func,last_index,initial_time,final_time)
    circle_drawer(coefficients)
