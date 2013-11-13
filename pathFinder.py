from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

x = np.array([ 2.,  1.,  1.,  2.,  2.,  4.,  4.,  3.])
y = np.array([ 1.,  2.,  3.,  4.,  2.,  3.,  2.,  1.])
plt.plot(x,y, label='poly')

t = np.arange(x.shape[0], dtype=float)
t /= t[-1]
nt = np.linspace(0, 1, 100)
x1 = scipy.interpolate.spline(t, x, nt)
y1 = scipy.interpolate.spline(t, y, nt)
plt.plot(x1, y1, label='range_spline')

t = np.zeros(x.shape)
t[1:] = np.sqrt((x[1:] - x[:-1])**2 + (y[1:] - y[:-1])**2)
t = np.cumsum(t)
t /= t[-1]
x2 = scipy.interpolate.spline(t, x, nt)
y2 = scipy.interpolate.spline(t, y, nt)
plt.plot(x2, y2, label='dist_spline')

plt.legend(loc='best')
plt.show()
