'TODO: check that the image exists'

import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_position(event, x, y, flags, pos):
    if event == cv2.EVENT_LBUTTONDOWN:
        pos[0].append(x)
        pos[1].append(y)

map = cv2.imread("map.png")
map_plt = plt.imread("map.png")
window = cv2.namedWindow("Caca")
cv2.imshow("Caca", map)

plt.interactive(True)
plt.imshow(map_plt)

shift = 0
xl = []
yl = []
t = np.linspace(0, 1, 1000)
cv2.setMouseCallback("Caca", get_position, [xl, yl])
while not (len(xl) - shift < 3):
    Px = (1-t)**3*xl[shift] + 3*(1-t)**2*t*xl[shift+1] 
    + 3*(1-t)*t**2*xl[shift+2] + t**3*xl[shift+3]
    Py = (1-t)**3*yl[shift] + 3*(1-t)**2*t*yl[shift+1] 
    + 3*(1-t)*t**2*yl[shift+2] + t**3*yl[shift+3]
    plt.plot(Px, Py)
    shift += 3
    print shift    
print xl
cv2.waitKey()
