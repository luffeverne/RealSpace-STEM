#!/usr/bin/python
# -*- coding: UTF-8 -*-

import abtem.structures
import ase.io
import ase.build


def handleDraw(filename, nx, ny, nz, u, v, w):
    crystal = ase.io.read(filename)
    # print(crystal.positions)

    crystal *= (nx, ny, nz)
    # view(crystal)

    crystal_uvw = ase.build.surface(crystal, indices=(u, v, w), layers=1, periodic=True)
    orthogonal_crystal_uvw = abtem.structures.orthogonalize_cell(crystal_uvw, max_repetitions=5)

    return orthogonal_crystal_uvw

