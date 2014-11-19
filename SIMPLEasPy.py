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

from StaggeredGrid import *

def main():
    
    grid = StaggeredGrid(10, 10)

if __name__ == "__main__":
    main()