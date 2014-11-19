# -*- coding: utf-8 -*-

"""

StaggeredGrid

Author: Adam O'Brien

This module is for storing the conserved variables of the Navier-Stokes 
equations on a staggered mesh, for use in the SIMPLE algorithm.

"""

import numpy as np

class StaggeredGrid(object):
    
    def __init__(self, nx, ny, x0 = 0., x1 = 1., y0 = 0., y1 = 1.):
        
        # These are the positions of the face centered values        
        
        xF = np.linspace(x0, x1, nx)
        yF = np.linspace(y0, y1, ny)
        
        # These are the positions of the cell centered values
        
        xP = []
        yP = []        
        
        for i in range(0, nx - 1):
            
            xP.append(0.5*(xF[i] + xF[i + 1]))
            
        for i in range(0, ny - 1):
            
            yP.append(0.5*(yF[i] + yF[i + 1]))
        
        self.xF, self.yF = np.meshgrid(xF, yF, indexing = 'ij')
        self.xP, self.yP = np.meshgrid(xP, yP, indexing = 'ij')

        # Initialize flow variables

        self.rho = 998.
        self.mu = 8.94e-4
        self.u = np.zeros((nx, ny))
        self.v = np.zeros((nx, ny))
        self.P = np.zeros((nx - 1, ny - 1))
        