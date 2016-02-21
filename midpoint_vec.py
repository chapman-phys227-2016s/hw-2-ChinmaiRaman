#! /usr/bin/env python

"""
File: midpoint_vec.py
Copyright (c) 2016 Chinmai Raman
License: MIT

Course: PHYS227
Assignment: 5.22
Date: Feb 20, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Estimates an integral using the midpoint rule for integration using three different implementations and compares their runtimes.
"""

import numpy as np
import math

def midpointint(f, a, b, n):
    """
    Estimates an integral using the midpoint rule for integration using a for loop
    """
    h = (b - a) / float(n)
    summation = 0
    for i in xrange(n):
        summation += f(a - h / 2.0 + (i + 1) * h)
    return summation * h

def midpointvectorized(f, a, b, n):
    """
    Estimates an integral using the midpoint rule for integration using math.sum
    """
    h = (b - a) / float(n)
    return h * sum(f(a - h / 2.0 + np.linspace(1, n, n) * h))

def midpointvectorized2(f, a, b, n):
    """
    Estimates an integral using the midpoint rule for integration using np.sum
    """
    h = (b - a) / float(n)
    return h * np.sum(f(a - h / 2.0 + np.linspace(1, n, n) * h))

def f(x):
    return x**2

def test_midpoint():
    assert(abs(midpointint(f, 0, 2, 10000) - (8 / 3.0)) < 1e-6)

def test_midpointvec():
    assert(abs(midpointvectorized(f, 0, 2, 10000) - (8 / 3.0)) < 1e-6)

def test_midpointvec2():
    assert(abs(midpointvectorized2(f, 0, 2, 10000) - (8 / 3.0)) < 1e-6)