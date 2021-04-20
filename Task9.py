from Task4 import Model
from Task2 import MyImage
from Task3 import Drawer
import numpy as np

model = Model()

model.load('Test_alien.obj', (0, 3, 6), -28, 450, -28, 700)
cords = model.getCords()
poligons = model.getPoligons()
points = model.getPoints()

drawer = Drawer()

image = MyImage(1000, 1000)

k = 0
for polygon in poligons:
    drawer.drawPolygon(model, polygon, image, (255, 255, 255))
    k += 1

image.save('Output/Task9_alien.jpg')