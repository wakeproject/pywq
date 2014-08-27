# -*- coding: utf-8 -*-

import numpy as np

from math import sqrt

def accelerationOf(unit, m1, m2):

    def acceleration(t, x):
        x1 = x[0]
        y1 = x[1]
        x2 = x[2]
        y2 = x[3]
        x3 = x[4]
        y3 = x[5]

        r12 = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        r13 = sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
        r21 = r12
        r23 = sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
        r31 = r13
        r32 = r23

        a12 = unit.G * m2 / r12 / r12
        a12x = a12 * (x2 - x1) / r12
        a12y = a12 * (y2 - y1) / r12

        a21 = unit.G * m1 / r21 / r21
        a21x = a21 * (x1 - x2) / r21
        a21y = a21 * (y1 - y2) / r21

        a31 = unit.G * m1 / r31 / r31
        a31x = a31 * (x1 - x3) / r31
        a31y = a31 * (y1 - y3) / r31

        a32 = unit.G * m2 / r32 / r32
        a32x = a32 * (x2 - x3) / r32
        a32y = a32 * (y2 - y3) / r32

        return np.array([a12x, a12y, a21x, a21y, a31x + a32x, a31y + a32y])

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
        x3  = phase[8]
        y3  = phase[9]
        vx3 = phase[10]
        vy3 = phase[11]

        r12 = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        r13 = sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
        r21 = r12
        r23 = sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
        r31 = r13
        r32 = r23

        a12 = unit.G * m2 / r12 / r12
        a12x = a12 * (x2 - x1) / r12
        a12y = a12 * (y2 - y1) / r12

        a21 = unit.G * m1 / r21 / r21
        a21x = a21 * (x1 - x2) / r21
        a21y = a21 * (y1 - y2) / r21

        a31 = unit.G * m1 / r31 / r31
        a31x = a31 * (x1 - x3) / r31
        a31y = a31 * (y1 - y3) / r31

        a32 = unit.G * m2 / r32 / r32
        a32x = a32 * (x2 - x3) / r32
        a32y = a32 * (y2 - y3) / r32

        return np.array([vx1, vy1, a12x, a12y,
                         vx2, vy2, a21x, a21y,
                         vx3, vy3, a31x + a32x, a31y + a32y])

    return derivative
