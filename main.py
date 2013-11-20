#!/bin/env python2
# -*- coding: utf-8 -*-

import pygame as pg
import numpy as np

# Save the stack_size last maps
stack_size = 15

def plot_bez(map, Px, Py):
    ''' Plot the bezier defined by Px, Py '''
    assert Px.size == Py.size
    pos = []
    for i in range(0, Px.size - 1):
        pos += [(Px[i], Py[i])]
    pg.draw.lines(map, (255,0,0), False, pos)

def plot_line(map, x, y):
    ''' Draw a line between the 2 last points of x and y '''
    pg.draw.line(map, 
                 (0,255,0),
                 (x[-2], y[-2]),(x[-1],y[-1]))

def redraw(map, x, y, map_init):
    ''' Redraws from scratch '''
    n = [0]
    map = map_init
    for i in range(0, x.size):
        n[0] += 1
        draw_once(map, x[:i], y[:i], n)


def draw_once(map, x, y, nval):
    ''' Analyses x and y to decide whether or not to draw sthg '''
    if x.size > 1:
        plot_line(map, x, y)
        if n[0] == 4:
            Px = a * x[-4] + b * x[-3] + c * x[-2] + d * x[-1]
            Py = a * y[-4] + b * y[-3] + c * y[-2] + d * y[-1]
            plot_bez(map, Px, Py)
            n[0] = 1

if __name__ == '__main__':
    screen = pg.display.set_mode((877, 620))
    map = pg.image.load("map_little.png").convert()
    map_init = pg.Surface.copy(map)
    screen.blit(map, (0, 0))
    pg.display.flip()
    running = 1

    x = np.array([])
    y = np.array([])
    
    nt = np.linspace(0, 1, 100)
    # Interpolation manuelle avec poignée de controle
    a = (1-nt)**3
    b = 3*(1-nt)**2*nt
    c = 3*(1-nt)*nt**2
    d = nt**3
    
    # Compte le nombre de points depuis le dernier tracé de bezier
    n = [0]
    
    while running:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            running = 0
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                # Left button clicked, we draw
                n[0]+=1
                x = np.append(x, event.pos[0])
                y = np.append(y, event.pos[1])
                draw_once(map, x, y, n)
                screen.blit(map, (0, 0))
                pg.display.flip()
            elif event.button == 3:
                # Right button clicked, we delete the last pt of x and y
                x = x[:-1]
                y = y[:-1]
                # We redraw everything from start
                redraw(map, x , y, map_init)
                screen.blit(map, (0, 0))
                pg.display.flip()
