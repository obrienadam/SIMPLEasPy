# -*- coding: utf-8 -*-

"""

SIMPLE

Author: Adam O'Brien

This module contains a number of functions pertinent to the SIMPLE method of
Patankar (1983)

"""

# Under-relaxation factor

alpha = 0.8

# Advection discretization in the x and y directions. These functions take
# velocity stencils as argumets.

def Ax(u, v, hx, hy):

    return 0.25/hy*((u[2][1] + u[1][1])**2 - (u[1][1] + u[0][1])**2) \
         + 0.25/hx*((u[1][2] + u[1][1])*(v[1][1] + v[0][1]) \
         - (u[1][0] + u[1][1])*(v[1][0] + v[0][0])
         )

def Ay(u, v, hx, hy):

    return 0.25/hy*((u[1][0] + u[1][1])*(v[1][1] + v[2][1]) \
         - (u[0][1] + u[0][0])*(v[1][1] + v[0][1])
         ) \
         + 0.25/hx*((v[1][2] + v[1][1])**2 - (v[1][1] + v[1][0])**2)

# Diffusion discretization in the x and y directions. These functions also take
# velocity stencils as arguments.

def Dx(u, hx, hy):

    return (u[2][1] + u[0][1] - 2.*u[1][1])/hx**2 + (u[1][2] + u[1][0] - 2.*u[1][1])/hy**2

def Dy(v, hx, hy):

    return (v[2][1] + v[0][1] - 2.*v[1][1])/hx**2 + (v[1][2] + v[1][0] - 2.*v[1][1])/hy**2


