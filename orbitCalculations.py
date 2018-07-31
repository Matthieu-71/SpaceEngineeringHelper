import numpy as np
from numpy import linalg as la
import math as m
import AnomalyConverter as ac
import imp
import matplotlib.pyplot as pl


# Authour : Matthieu Durand
# Creator date : July 30 2018
# Script to calculate perital position using various methods

def stateVector(a,ec,inc,RA,Ap,TA):
    # This functions returns the state vectors (radius and velocity) given six perital elements
    # Semi-major axis, eccentricity, inclination, RAAN, argument of perigee, true anomaly
	
	p = a*(1 - ec**2) # Semi-latus rectum in km
	h = m.sqrt(mu_Earth*p) # Specific relative angular momentum, in km2 s-1
	radius = a*(1 - ec**2)/(1 + ec*m.cos(TA)) # Radius in kilometres, found with true anomaly
	
	perR = (h**2/mu_Earth)*(1/(1 + ec**m.cos(TA)))*np.array([m.cos(TA),m.sin(TA),0]) # Compute radius in perifocal frame
	geoR = np.array([perR[0]*(m.cos(Ap)*m.cos(RA)-m.sin(Ap)*m.cos(inc)*m.sin(RA)) - perR[1]*(m.sin(Ap)*m.cos(RA)+m.cos(Ap)*m.cos(inc)*m.sin(RA)),
					 perR[0]*(m.cos(Ap)*m.sin(RA)-m.sin(Ap)*m.cos(inc)*m.cos(RA)) + perR[1]*(m.cos(Ap)*m.cos(inc)*m.cos(RA)-m.sin(Ap)*m.sin(RA)),
					 perR[0]*(m.sin(Ap)*m.sin(inc))+perR[1]*(m.cos(Ap)*m.sin(inc))]) # Compute radius in geocentric frame
	
	perV = (mu_Earth/h)*np.array([-m.sin(TA),ec + m.cos(TA),0]) # Compute velocity in perifocal frame 
	geoV = np.array([perV[0]*(m.cos(Ap)*m.cos(RA)-m.sin(Ap)*m.cos(inc)*m.sin(RA)) - perV[1]*(m.sin(Ap)*m.cos(RA)+m.cos(Ap)*m.cos(inc)*m.sin(RA)),
					 perV[0]*(m.cos(Ap)*m.sin(RA)-m.sin(Ap)*m.cos(inc)*m.cos(RA)) + perV[1]*(m.cos(Ap)*m.cos(inc)*m.cos(RA)-m.sin(Ap)*m.sin(RA)),
					 perV[0]*(m.sin(Ap)*m.sin(inc))+perV[1]*(m.cos(Ap)*m.sin(inc))]) # Compute radius in geocentric frame
					 
	return perR
	

mu_Earth = 3.986004418*(10**5) # Earth's standard gravitational parameter, in km3 s-2

sma = 42000 # In km
ecc = 0.01
inc = 0
raa = 0
aop = 0
tra = np.linspace(0, 2*np.pi, num=100) # In radians

i = 0
X = np.zeros(100)
Y = np.zeros(100)
for i in range(0,99):
	temp = stateVector(sma,ecc,inc,raa,aop,tra[i])
	X[i] = temp[0]
	Y[i] = temp[1]
	
pl.plot(X,Y)
pl.show()
# stateVector(sma,ecc,inc,raa,aop,tra)
# new = ac.Mean2Ecce(0.488692,ecc)
