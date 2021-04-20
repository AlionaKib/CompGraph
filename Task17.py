from Task4 import Model
from Task2 import MyImage
from Task3 import Drawer
import random
import numpy as np

model = Model()

model.load('Test_alien.obj', (0, 3, 6), (0, 0, 1))
model.setScale(-28, -28, 450, 700)
cords = model.getCords()
poligons = model.getPoligons()
points = model.getPoints()
cos_lights = model.getCos_light()

model.rotate(0, 90, 0)

drawer = Drawer()

N = 1000
M = 1000

image = MyImage(N, M)

k = 0
for polygon in poligons:
    if cos_lights[k] < 0:
        drawer.drawPolygon(model, polygon, image, (int(-255 * cos_lights[k]), int(-255 * cos_lights[k]), int(-255 * cos_lights[k])))
    k += 1

image.save('Output/Task17_alien.jpg')