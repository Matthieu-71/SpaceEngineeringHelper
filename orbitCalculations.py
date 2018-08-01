import numpy as np
from numpy import linalg as la
import math as m
import AnomalyConverter as ac
import SpaceConstants as sc
import imp
import matplotlib.pyplot as pl
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import SphereCreator


# Authour : Matthieu Durand
# Creator date : July 30 2018
# Script to calculate perital position using various methods

def semiLat(a,e):
        # Calculates the semi-latus rectum in kilometers
        # a - semimajor axis, e - eccentricity
        p = a*(1 - e**2)
        return p

def speRAM(p,body):
        # Calculates the specific angular momentum of a satellite about a body
        # p - semilatus rectum [km], body - name as a string
        h = m.sqrt(getattr(sc.mu,body)*p)
        return h

def stateVector(a,ec,inc,RA,Ap,TA):
    # This functions returns the state vectors (radius and velocity) given six orbital elements
    # Semi-major axis, eccentricity, inclination, RAAN, argument of perigee, true anomaly
	
	p = semiLat(a,ec) # Semi-latus rectum in km
	#h = m.sqrt(mu_Earth*p) # Specific relative angular momentum, in km2 s-1
	h = speRAM(p,'Earth')
	radius = a*(1 - ec**2)/(1 + ec*m.cos(TA)) # Radius in kilometres, found with true anomaly
	
	perR = (h**2/mu_Earth)*(1/(1 + ec*m.cos(TA)))*np.array([m.cos(TA),m.sin(TA),0]) # Compute radius in perifocal frame
	geoR = np.array([perR[0]*(m.cos(Ap)*m.cos(RA)-m.sin(Ap)*m.cos(inc)*m.sin(RA)) - perR[1]*(m.sin(Ap)*m.cos(RA)+m.cos(Ap)*m.cos(inc)*m.sin(RA)),
					 perR[0]*(m.cos(Ap)*m.sin(RA)-m.sin(Ap)*m.cos(inc)*m.cos(RA)) + perR[1]*(m.cos(Ap)*m.cos(inc)*m.cos(RA)-m.sin(Ap)*m.sin(RA)),
					 perR[0]*(m.sin(Ap)*m.sin(inc))+perR[1]*(m.cos(Ap)*m.sin(inc))]) # Compute radius in geocentric frame
	
	perV = (mu_Earth/h)*np.array([-m.sin(TA),ec + m.cos(TA),0]) # Compute velocity in perifocal frame 
	geoV = np.array([perV[0]*(m.cos(Ap)*m.cos(RA)-m.sin(Ap)*m.cos(inc)*m.sin(RA)) - perV[1]*(m.sin(Ap)*m.cos(RA)+m.cos(Ap)*m.cos(inc)*m.sin(RA)),
					 perV[0]*(m.cos(Ap)*m.sin(RA)-m.sin(Ap)*m.cos(inc)*m.cos(RA)) + perV[1]*(m.cos(Ap)*m.cos(inc)*m.cos(RA)-m.sin(Ap)*m.sin(RA)),
					 perV[0]*(m.sin(Ap)*m.sin(inc))+perV[1]*(m.cos(Ap)*m.sin(inc))]) # Compute velocity vector in geocentric frame
					 
	return geoR
	

mu_Earth = sc.mu.Earth # Earth's standard gravitational parameter, in km3 s-2

sma = 10000 # In km
ecc = np.random.random()
inc = np.random.random()*2*np.pi
raa = np.random.random()*2*np.pi
aop = np.random.random()*2*np.pi
tra = np.linspace(0, 2*np.pi, num=100) # In radians
print("Orbit generated for: e = " + str(ecc) + ", i = " + str(inc*180/np.pi) + " deg, RAAN = " + str(raa*180/np.pi) + " deg, AoP = " + str(aop*180/np.pi) + " deg.")

i = 0
X = np.zeros(100)
Y = np.zeros(100)
Z = np.zeros(100)
for i in range(0,100):
        temp = stateVector(sma,ecc,inc,raa,aop,tra[i])
        X[i] = temp[0]
        Y[i] = temp[1]
        Z[i] = temp[2]

fig = pl.figure()
ax = fig.gca(projection='3d')
pl.plot(X,Y,Z, color='k')
[x,y,z] = SphereCreator.showBody('Earth')

ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
pl.show()
# stateVector(sma,ecc,inc,raa,aop,tra)
# new = ac.Mean2Ecce(0.488692,ecc)
