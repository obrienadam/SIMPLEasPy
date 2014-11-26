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

        # Basic spacing

        self.hx = (x1 - x0)/float(nx - 1)
        self.hy = (y1 - y0)/float(ny - 1)

        # Compute the grid nodes/vertices

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

        # Set physical constants

        self.rho = 998.
        self.mu = 8.94e-4

        # Initial conditions

        self.u = np.zeros((nx, ny - 1))
        self.v = np.zeros((nx - 1, ny))
        self.p = np.zeros((nx - 1, ny - 1))

        # Allocate memory for the predictor steps

        self.ustar = self.u
        self.vstar = self.v


        # Set boundaries

        self.boundaries = {"East" : ["Outlet", 0.],
                           "West" : ["Inlet", 1.],
                           "North" : ["Wall", 0.],
                           "South" : ["Wall", 0.]}

        self.setBoundaries()

    def displayGrid(self):

        plt.plot(self.xNodes, self.yNodes, 'b',
                 np.transpose(self.xNodes), np.transpose(self.yNodes), 'b',
                 self.xPgrid, self.yPgrid, 'or',
                 self.xUgrid, self.yUgrid, 'xb',
                 self.xVgrid, self.yVgrid, '.b')

        plt.xlabel('x (m)')
        plt.ylabel('y (m)')

        plt.show()

    def displayCurrentSolution(self):

        plt.contourf(self.xUgrid, self.yUgrid, self.u)

        plt.xlabel('x (m)')
        plt.ylabel('y (m)')

        plt.show()

    def getUstencil(self, i, j):

        northU, southU = self.getNorthSouthU(i, j)

        return [self.u[i-1][j], [southU, self.u[i][j], northU], self.u[i+1][j]], \
               [[self.v[i-1], self.v[i][j]], [self.v[i-1][j+1], self.v[i][j+1]]]

    def getNorthSouthU(self, i, j):

        if j == len(self.u[i]) - 1:

            northU = -self.u[i][j]

        else:

            northU = self.u[i][j+1]

        if j == 0:

            southU = -self.u[i][j]

        else:

            southU = self.u[i][j-1]

        return northU, southU

    # Boundary condition helper methods

    def setBoundaries(self):

        self.setEastBoundary()
        self.setWestBoundary()
        self.setNorthBoundary()
        self.setSouthBoundary()

    def setEastBoundary(self):

        upperI = len(self.u) - 1

        for j in range(0, len(self.u[upperI])):

            self.u[upperI][j] = self.boundaries["East"][1]

    def setWestBoundary(self):

        for j in range(0, len(self.u[0])):

            self.u[0][j] = self.boundaries["West"][1]


    def setNorthBoundary(self):

        upperJ = len(self.v[0]) - 1

        for i in range(0, len(self.v)):

            self.v[i][upperJ] = self.boundaries["North"][1]

    def setSouthBoundary(self):

        for i in range(0, len(self.v)):

            self.v[i][0] = self.boundaries["South"][1]