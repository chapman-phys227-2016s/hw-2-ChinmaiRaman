#! /usr/bin/env python

"""
File: Lagrange_poly2.py
Copyright (c) 2016 Chinmai Raman
License: MIT

Course: PHYS227
Assignment: 5.24
Date: Feb 20, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Plots Lagrange's interpolating polynomial
"""

import numpy as np

def graph(f, n, xmin, xmax, resolution = 1001):
    fig = plt.figure(1)
    xpactual = np.linspace(xmin, xmax, n)
    ypactual = f(xpactual)
    xp = np.linspace(xmin, xmax, resolution)
    yp = np.array([p_L(x, xpactual, ypactual) for x in xp])
    plt.plot(xpactual, ypactual, 'ro')
    plt.plot(xp, yp, 'b-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([xmin, xmax, min(ypactual) - 0.3, max(ypactual) + 0.3])
    plt.title('f(x) and interpolation points')
    plt.show(fig)
    
def multigraph(f, n, xmin, xmax, c, resolution = 1001):
    i = 0
    for elem in n:
        fig = plt.figure(1)
        xpactual = np.linspace(xmin, xmax, elem)
        ypactual = f(xpactual)
        xp = np.linspace(xmin, xmax, resolution)
        yp = np.array([p_L(x, xpactual, ypactual) for x in xp])
        plt.plot(xpactual, ypactual, 'ro')
        plt.plot(xp, yp, c[i])
        i += 1
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([xmin, xmax, min(ypactual) - 0.3, max(ypactual) + 0.3])
    plt.title('f(x) and interpolation points')
    plt.show(fig)

def f(x):
    return np.sin(x)

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

def test_p_L(xp, yp):
    for i in xrange(len(yp)):
        assert(abs(p_L(xp[i], xp, yp) - yp[i]) < 1e-3), 'Failure'

if __name__ == '__main__':
    print 'run as program'
    xp = np.linspace(0, np.pi, 5)
    yp = np.sin(xp)
    test_p_L(xp, yp)
    graph(f, 5, 0, np.pi)