import numpy as np
import math

# Authour : Matthieu Durand
# Creator date : July 30 2018
# Script contains functions to convert between true(T), mean(M) and eccentric(E) anomalies
# In all the functions: E, T, and M are in radians, and ec is the eccentricity of the ellipse/orbit

def Mean2Ecce(M,ec):
    # Solves Kepler's equation, f(E) = E - esin(E) - M, using the Newton-Raphson method
    E = -ec*math.sin(M)
    diff = 1
    n = 1
    while abs(diff) > 10**-9:
        diff = (E - ec*math.sin(E) - M)/(1 - ec*math.cos(E))
        E = E - diff
        n += 1
    print(E)
    return E

def Ecce2Mean(E,ec):
    # Calculates the eccentric anomaly using Kepler's equation
    M = E - ec*math.sin(E)
    print(M)
    return M
    
def Ecce2True(E,ec):
    # Calculates the true anomaly from the eccentric anomaly
    T = math.acos((math.cos(E) - ec)/(1 - ec*math.cos(E)))
    print(T)
    return T

def Ecce2True_2(E,ec):
    # Calculates the true anomaly from the eccentric anomaly using the arctan method
    T = 2*math.atan2(math.sqrt(1+ec)*math.sin(E/2),math.sqrt(1-ec)*math.cos(E/2))
    print(T)
    return T

def True2Ecce(T,ec):
    # Calculates the eccentric anomaly from the true anomaly
    E = math.cos(T)*(1 - ec*math.cos(E))/(math.cos(E) - ec)
    print(E)
    return E

def True2Mean(T,ec):
    # Calculates the mean anomaly from the true anomaly
    M = Ecce2Mean(True2Ecce(T,ec),ec)
    print(M)
    return M

def Mean2True(M,ec):
    # Calculates the true anomaly from the mean anomaly
    T = Ecce2True(Mean2Ecce(M,ec),ec)
    print(T)
    return T
