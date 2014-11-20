# -*- coding: utf-8 -*-

"""

StaggeredGrid

Author: Adam O'Brien

This module is for storing the conserved variables of the Navier-Stokes
equations on a staggered mesh, for use in the SIMPLE algorithm.

"""

import numpy as np
import matplotlib.pyplot as plt

class StaggeredGrid(object):

    def __init__(self, nx, ny, x0 = 0., x1 = 1., y0 = 0., y1 = 1.):

        # Compute the cell nodes/vertices

        xNodes = np.linspace(x0, x1, nx)
        yNodes = np.linspace(y0, y1, ny)

        self.xNodes, self.yNodes = np.meshgrid(xNodes, yNodes, indexing = 'ij')

        # Compute x coordinates for cell centered values

        xC = []

        for i in range(0, nx - 1):

            xC.append(0.5*(xNodes[i] + xNodes[i + 1]))

        # Compute y coordinates for cell centered values

        yC = []

        for j in range(0, ny - 1):

            yC.append(0.5*(yNodes[j] + yNodes[j + 1]))

        # Mesh all grids

        self.xPgrid, self.yPgrid = np.meshgrid(xC, yC, indexing = 'ij')
        self.xUgrid, self.yUgrid = np.meshgrid(xNodes, yC, indexing = 'ij')
        self.xVgrid, self.yVgrid = np.meshgrid(xC, yNodes, indexing = 'ij')

        # Set boundaries

        self.boundaries = {"East" : "Inlet",
                           "West" : "Outlet",
                           "North" : "Wall",
                           "South" : "Wall"}

        # Set physical constants

        self.rho = 998.
        self.mu = 8.94e-4

        # Initial conditions

        self.u = np.zeros((nx, ny - 1))
        self.v = np.zeros((nx - 1, ny))
        self.p = np.zeros((nx - 1, ny - 1))

    def displayGrid(self):

        plt.plot(self.xNodes, self.yNodes, 'b',
                 np.transpose(self.xNodes), np.transpose(self.yNodes), 'b',
                 self.xPgrid, self.yPgrid, 'or',
                 self.xUgrid, self.yUgrid, 'xb',
                 self.xVgrid, self.yVgrid, '.b')

        plt.xlabel('x (m)')
        plt.ylabel('y (m)')

        plt.show()
