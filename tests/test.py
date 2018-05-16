#!/usr/bin/env python

from paxes import inertia_tensor
import numpy as np

x = np.array([1.0, 2.0])
y = np.array([2.0, 3.0])
result = inertia_tensor.axpy(3, x, y)
print(result)
