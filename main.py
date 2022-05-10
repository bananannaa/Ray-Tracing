import pygame
from pygame import gfxdraw
import math

import vector
import shapes

class Ray:
    def __init__(self, x, y):
        self.pos = vector.Vector3(x, y, 0)
        self.stopped = False
        self.inshape = False
        self.colour = (0, 0, 0)

    def update(self, shapes, max_length):
        if self.stopped or self.pos.z >= max_length:
            return
        self.pos.z += 1
        for shape in shapes:
            if self.pos.distance_to(shape.centre) <= shape.radius:
                self.stopped = True
                self.inshape = True
                self.colour = shape.colour

width = 200
height = 200

win = pygame.display.set_mode((width, height))
sphere1 = shapes.Sphere(vector.Vector3(100, 100, 50), 20, (255, 0, 0))
sphere2 = shapes.Sphere(vector.Vector3(30, 30, 50), 10, (0, 255, 0))
shapes = [sphere1, sphere2]

rays = [Ray(x % width, x // width) for x in range(width * height)]

for i in range(100):
    for ray in rays:
        ray.update(shapes, 60)

for ray in rays:
    if ray.inshape:
        factor = (ray.pos.z / 25) ** 2
        print(factor)
        r = min(255, ray.colour[0] / factor)
        g = min(255, ray.colour[1] / factor)
        b = min(255, ray.colour[2] / factor)
        print(r, g, b)
        pygame.gfxdraw.pixel(win, ray.pos.x, ray.pos.y, (r, g, b))
        
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
