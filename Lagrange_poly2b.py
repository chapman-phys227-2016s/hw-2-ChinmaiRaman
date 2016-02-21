#! /usr/bin/env python

"""
File: Lagrange_poly2b.py
Copyright (c) 2016 Chinmai Raman
License: MIT

Course: PHYS227
Assignment: 5.25
Date: Feb 20, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Investigates the behavior of Lagrange's interpolating polynomials
"""

import numpy as np
from matplotlib.pylab import *

import Lagrange_poly2 as p1

def f(x):
    return np.absolute(x)