from Task4 import Model
from Task2 import MyImage
from Task3 import Drawer
import random
import numpy as np

model = Model()

model.load('Test_alien.obj', (0, 3, 6), -28, 450, -28, 700, (0, 0, 1))
cords = model.getCords()
poligons = model.getPoligons()
points = model.getPoints()
cos_lights = model.getCos_light()

drawer = Drawer()

image = MyImage(1000, 1000)

k = 0
for polygon in poligons:
    if cos_lights[k] < 0:
        drawer.drawPolygon(model, polygon, image, (int(-255 * cos_lights[k]), int(-255 * cos_lights[k]), int(-255 * cos_lights[k])))
    k += 1

image.save('Output/Task14_alien.jpg')
