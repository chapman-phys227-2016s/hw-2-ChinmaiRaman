#! /usr/bin/env python

"""
File: Lagrange_poly1.py
Copyright (c) 2016 Chinmai Raman
License: MIT

Course: PHYS227
Assignment: 5.23
Date: Feb 20, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Implements Lagrange's interpolation formula
"""

import numpy as np

def p_L(x, xp, yp):
    """
    Returns the polynomial pL(x), known as Lagrange's interpolation formula
    """
    summation = 0.0
    for k in xrange(len(yp)):
        summation += L_k(x, k, xp, yp) * yp[k]
    return summation

def L_k(x, k, xp, yp):
    """
    Returns the product that is used in calculating Lagrange's interpolation formula
    """
    product = 1.0
    for i in xrange(len(xp)):
        if i == k:
            continue
        product *= (x - xp[i]) / float(xp[k] - xp[i])
    return product

def test_L():
    xp = np.asarray([2, 3])
    yp = np.asarray([])
    assert(abs(L_k(-1, 1, xp, yp) - (-3)) < 1e-3)

def test_p_L():
    for i in xrange(len(yp)):
        assert(abs(p_L(xp[i], xp, yp) - yp[i]) < 1e-3), 'Failure'

xp = np.linspace(0, np.pi, 5)
yp = np.sin(xp)
test_p_L(xp, yp)

assert(abs(p_L(np.pi * 0.375, xp, yp) - np.sin(0.375 * np.pi)) < 1e-3)