#! /usr/bin/env python

"""
File: fit_pendulum_data.py
Copyright (c) 2016 Chinmai Raman
License: MIT

Course: PHYS227
Assignment: 5.18
Date: Feb 20, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Fits polynomials of varying degrees to experimental data
"""

import numpy as np


def extract_data(filename = 'pendulum.dat'):
    infile = open(filename, 'r')
    infile.readline()
    L = []
    T = []
    for line in infile:
        data = line.split()
        L.append(float(data[0]))
        T.append(float(data[1]))
    infile.close()
    L = np.asarray(L)
    T = np.asarray(T)
    return L, T

D = extract_data()
coeff1 = np.polyfit(D[0], D[1], 1)
p1 = np.poly1d(coeff1)
y_fit1 = p1(D[0])

coeff2 = np.polyfit(D[0], D[1], 2)
p2 = np.poly1d(coeff2)
y_fit2 = p2(D[0])

coeff3 = np.polyfit(D[0], D[1], 3)
p3 = np.poly1d(coeff3)
y_fit3 = p3(D[0])