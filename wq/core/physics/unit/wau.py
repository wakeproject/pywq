# -*- coding: utf-8 -*-

import wq.core.physics.unit.si
import wq.core.universe.wahlque.planet as p


def fromAU_T(t):
    return t * si.fromAU_T(1) / p.period