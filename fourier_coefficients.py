import scipy
from scipy.integrate import quad
from math import pi, e

def complex_quad(func, a, b, **kwargs):
    real_func = lambda t: scipy.real(func(t))
    imag_func = lambda t: scipy.imag(func(t))
    real_integral = quad(real_func, a, b, **kwargs)
    imag_integral = quad(imag_func, a, b, **kwargs)
    return complex(real_integral[0] + 1j*imag_integral[0])

def fourier_coefficient(func, index):
    integrand = lambda t: func(t) * e**(-2 * pi * index * t * 1j)
    return complex_quad(integrand,0,1)

def fourier_coefficients(func, last_index):
    coefficients = {}
    indices = range(-last_index, last_index)
    for i in indices:
        coefficients[i] = fourier_coefficient(func,i)
    return coefficients
