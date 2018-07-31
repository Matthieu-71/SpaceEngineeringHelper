import numpy as np
import math
import AnomalyConverter as ac

# Authour : Matthieu Durand
# Creator date : July 30 2018
# Script to calculate orbital position using various methods

def stateVector(a,ec,inc,RA,Ap,TA):
    # This functions returns the state vectors (radius and velocity) given six orbital elements
    # Semi-major axis, eccentricity, inclination, RAAN, argument of perigee, true anomaly
    radius = a*(1 - ec**2)/(1 + ec*math.cos(TA)) # Radius in kilometres, found with true anomaly
    orbR = radius*np.array([math.cos(TA),math.sin(TA),0]) # Radius in km, in orbital frame
    bodR = np.array([orbR[1]*(math.cos(Ap)*math.cos(RA)-math.sin(Ap)*math.cos(inc)*math.sin(RA)) - orbR[2]*(math.sin(Ap)*math.cos(RA)+math.cos(Ap)*math.cos(inc)*math.sin(RA)),
                     orbR[1]*(math.cos(Ap)*math.sin(RA)-math.sin(Ap)*math.cos(inc)*math.cos(RA)) + orbR[2]*(math.cos(Ap)*math.cos(inc)*math.cos(RA)-math.sin(Ap)*math.sin(RA)),
                     orbR[1]*(math.sin(Ap)*math.sin(inc))+orbR[2]*(math.cos(Ap)*math.sin(inc))])
    
    radius = radius*1000 # In metres
    
    velocity = math.sqrt(mu_Earth*((2/radius) - 1/(a*1000))) # In m s-1
    velocity = velocity/1000

    b = a*math.sqrt(1 - ec**2) # Semi-minor axis, in km
    p = a*(1 - ec**2) # Semi-latus rectum in km
    h = math.sqrt(mu_Earth*(p*1000)) # Specific relative angular momentum, in m2 s-1

    #print(b,p,h)
    #print(radius,velocity)
    print(orbR)
    print(bodR)

mu_Earth = 3.986004418*(10**14) # Earth's standard gravitational parameter, in m3 s-2

sma = 10000 # In km
ecc = 0.1
inc = 0
raa = 0
aop = 0
tra = np.pi # In radians

stateVector(sma,ecc,inc,raa,aop,tra)
# new = ac.Mean2Ecce(0.488692,ecc)
