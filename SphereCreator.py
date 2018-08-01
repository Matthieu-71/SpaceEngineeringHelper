from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import SpaceConstants as sc


def showBody(body):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    bodyRad = getattr(sc.AvgRad,body)

    x = bodyRad * np.outer(np.cos(u), np.sin(v))
    y = bodyRad * np.outer(np.sin(u), np.sin(v))
    z = bodyRad * np.outer(np.ones(np.size(u)), np.cos(v))
    #ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
    return x,y,z 
    #plt.show()
