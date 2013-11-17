'TODO: check that the image exists'

import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
'This function gets the position and appends it to pos list'
def get_position(event, x, y, flags, pos):
    if event == cv2.EVENT_LBUTTONDOWN:
        pos[0].append(x)
        pos[1].append(y)

map = cv2.imread("map.png")
map_plt = plt.imread("map.png")
window = cv2.namedWindow('Caca')
cv2.imshow('Caca', map)
'pos = [ x list, y list]'
while True:
    pos = [[],[]]
    cv2.setMouseCallback('Caca', get_position, pos)
    cv2.waitKey(0)
    
    print "Positions acquired, now calculating the splines"
    
    x = np.array(pos[0])
    y = np.array(pos[1])
    'plt.plot(x,y, label="poly")'
    nt = np.linspace(0, 1, 1000)

    t = np.zeros(x.shape)
    t[1:] = np.sqrt((x[1:] - x[:-1])**2 + (y[1:] - y[:-1])**2)
    t = np.cumsum(t)
    t /= t[-1]
    x2 = scipy.interpolate.spline(t, x, nt)
    y2 = scipy.interpolate.spline(t, y, nt)
    plt.plot(x2, y2)
    
    plt.legend(loc='best')
    plt.imshow(map_plt)
    plt.show()
