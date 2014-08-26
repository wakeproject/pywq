# -*- coding: utf-8 -*-

import numpy as np

from math import sqrt

def accelerationOf(unit, m1, m2):

    def acceleration(t, x):
        x1 = x[0]
        y1 = x[1]
        x2 = x[2]
        y2 = x[3]

        r12 = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        r21 = r12

        a12 = unit.G * m1 / r12 / r12
        a12x = a12 * (x2 - x1) / r12
        a12y = a12 * (y2 - y1) / r12

        a21 = unit.G * m2 / r21 / r21
        a21x = a21 * (x1 - x2) / r21
        a21y = a21 * (y1 - y2) / r21

        return np.array([a12x, a12y, a21x, a21y])

    return acceleration
    
def derivativeOf(unit, m1, m2):

    def derivative(t, phase):
        x1  = phase[0]
        y1  = phase[1]
        vx1 = phase[2]
        vy1 = phase[3]
        x2  = phase[4]
        y2  = phase[5]
        vx2 = phase[6]
        vy2 = phase[7]

        r12 = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        r21 = r12

        a12 = unit.G * m1 / r12 / r12
        a12x = a12 * (x2 - x1) / r12
        a12y = a12 * (y2 - y1) / r12

        a21 = unit.G * m2 / r21 / r21
        a21x = a21 * (x1 - x2) / r21
        a21y = a21 * (y1 - y2) / r21

        return np.array([vx1, vy1, a12x, a12y, vx2, vy2, a21x, a21y])

    return derivative
