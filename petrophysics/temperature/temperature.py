#__all__ = ['tf', 'gradient', 'horner']

import numpy as np
'''
List of functions:
tf - formation temperature
gradient -
horner -
'''

def tf(t0, gradient, depth):
    '''
    tf(t0, depth, gradient)
    *Input parameters:
     - t0 - annual surface mean temperature [C] or [F]
     - gradient - [C/m] or [F/ft]
     - depth - at which temperature will be calculated [m] or [ft]
    *Returns:
     - tf - formation temperature [C] or [ft] based on temperature gradient
    '''
    tf = t0 + depth * gradient
    return tf

def gradient(t0, tf, depth):
    '''
    gradient(t0, tf, depth)
    *Input parameters
     - t0 - annual surface mean temperature [C] or [F]
     - tf - formation temperature [C] or [ft]
     - depth - at which temperatures will be calculated [m] or [ft]
    *Returns:
     - gradient - [C/m] or [F/ft]
    '''
    gradient = (tf - t0) / depth
    return gradient

def horner(circulation_time, times, temp):
    '''
    horner_bht_temp (circulation_time, times, temp)
    *Input parameters:
    - circulation_time - hours from last circulation;
    - times - total time since circulation stopped at 1st Run, 2nd Run and so on ...
    - temp - a list o temperatures coresponding to 1st Run, 2nd Run and so on ...
    *Returns:
    - horner_temp - formation temperature estimated by Horner method (thermometer readings
    from different runs)
    *Exemple of usage:
    horner(6, (7.0,11.5,19.5), (100,105,108))
        where:
        circulation_time = 6           # time since circulation stopped (hours)
        times = (7.0,11.5,19.5)        # total time since circulation stopped at 1st, 2nd, 3rd RUN (hours)
        temp=(100,105,108)             # temperatures recorded at 1st, 2nd, 3rd RUN (Celsius degrees)
    '''
    horner_time = np.array(times) / (circulation_time + np.array(times))
    slope,intercept = np.polyfit (np.log(horner_time), temp, 1)
    horner_temp=round(slope*np.log(1) +intercept,2)
    return horner_temp
