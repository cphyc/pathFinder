from PIL import Image, ImageDraw
import pygame as pg
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate
def make_bezier(xys):
    # xys should be a sequence of 2-tuples (Bezier control points)
    n = len(xys)
    combinations = pascal_row(n-1)
    def bezier(ts):
        # This uses the generalized formula for bezier curves
        # http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization
        result = []
        for t in ts:
            tpowers = (t**i for i in range(n))
            upowers = reversed([(1-t)**i for i in range(n)])
            coefs = [c*a*b for c, a, b in zip(combinations, tpowers, upowers)]
            result.append(
                tuple(sum([coef*p for coef, p in zip(coefs, ps)]) for ps in zip(*xys)))
        return result
    return bezier

def quad_bezier(ptlist, t):
    assert len(ptlist) == 4
    p1 = ptlist[0]
    p2 = ptlist[1]
    p3 = ptlist[2]
    p4 = ptlist[3]
    print p1, p2, p3, p4
    Px = (1-t)**3*p1[0] + 3*(1-t)**2*t*p2[0] 
    + 3*(1-t)*t**2*p3[0] + t**3*p4[0]
    Py = (1-t)**3*p1[1] + 3*(1-t)**2*t*p2[1]
    + 3*(1-t)*t**2*p3[1] + t**3*p4[1]
    return [Px, Py]

def pascal_row(n):
    # This returns the nth row of Pascal's Triangle
    result = [1]
    x, numerator = 1, n
    for denominator in range(1, n//2+1):
        # print(numerator,denominator,x)
        x *= numerator
        x /= denominator
        result.append(x)
        numerator -= 1
    if n&1 == 0:
        # n is even
        result.extend(reversed(result[:-1]))
    else:
        result.extend(reversed(result)) 
    return result

if __name__ == '__main__':
    screen = pg.display.set_mode((877, 620))
    map = pg.image.load("map_little.png").convert()
    screen.blit(map, (0, 0))
    pg.display.flip()
    running = 1

    x = np.array([])
    y = np.array([])
    map = plt.imread("map_little.png")
    plt.imshow(map)
    while running:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            running = 0
        elif event.type == pg.MOUSEBUTTONUP:
            x = np.append(x, event.pos[0])
            y = np.append(y, event.pos[1])

    nt = np.linspace(0, 1, 1000)
    t = np.zeros(x.shape)
    t[1:] = np.sqrt((x[1:] - x[:-1])**2 + (y[1:] - y[:-1])**2)
    t = np.cumsum(t)
    t /= t[-1]
    x2 = scipy.interpolate.spline(t, x, nt)
    y2 = scipy.interpolate.spline(t, y, nt)
    plt.plot(x,y)
    plt.plot(x2, y2)
    plt.show()
