from Task4 import Model
from Task2 import MyImage
from Task3 import Drawer
import numpy as np

model = Model()

model.load('Test_alien.obj', (0, 3, 6))
model.setScale(-28, -28, 450, 700, False)
poligons = model.getPoligons()
points = model.getPoints()

drawer = Drawer()

image = MyImage(1000, 1000)

for poligon in poligons:
    drawer.line4(points[poligon[0] - 1], points[poligon[1] - 1], image, (255, 255, 255))
    drawer.line4(points[poligon[1] - 1], points[poligon[2] - 1], image, (255, 255, 255))
    drawer.line4(points[poligon[2] - 1], points[poligon[0] - 1], image, (255, 255, 255))

image.save('Output/Task7_alien.jpg')
