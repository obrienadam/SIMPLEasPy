#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""

SIMPLEasPy

Author: Adam O'Brien

This program uses the SIMPLE method (Patankar 1983) to solve simple
incompressible Navier-Stokes problems on cartesian meshes. The objective is to
use this program to test out surface tension models and immersed boundary
methods.

"""

from StaggeredGrid import StaggeredGrid
from SIMPLE import *

def main():

    grid = StaggeredGrid(20, 20)

    momentumPredictor(grid)

if __name__ == "__main__":
    main()