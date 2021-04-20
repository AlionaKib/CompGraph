from Task4 import Model
from Task2 import MyImage
from Task3 import Drawer
import numpy as np

model = Model()
# model.load('Test_rabbit.obj', (0,3,6))
# cords = model.getCords()
# poligons = model.getPoligons()
#
# drawer = Drawer()
#
# image = MyImage(1000, 1000)
# points = np.zeros(len(cords), dtype=tuple)
#
# k = 0
# for cord in cords:
#     x = int(8000 * (-cord[0]) + 500)
#     y = int(8000 * (-cord[1]) + 900)
#     points[k] = (x, y)
#     k += 1
#
# for poligon in poligons:
#     drawer.line4(points[poligon[0] - 1], points[poligon[1] - 1], image, (255, 255, 255))
#     drawer.line4(points[poligon[1] - 1], points[poligon[2] - 1], image, (255, 255, 255))
#     drawer.line4(points[poligon[2] - 1], points[poligon[0] - 1], image, (255, 255, 255))
#
# image.save('Output/Task7_rabbit.jpg')

model.load('Test_alien.obj', (0, 3, 6), -28, 450, -28, 700, (0, 0, 1))
cords = model.getCords()
poligons = model.getPoligons()
points = model.getPoints()

drawer = Drawer()

image = MyImage(1000, 1000)

for poligon in poligons:
    drawer.line4(points[poligon[0] - 1], points[poligon[1] - 1], image, (255, 255, 255))
    drawer.line4(points[poligon[1] - 1], points[poligon[2] - 1], image, (255, 255, 255))
    drawer.line4(points[poligon[2] - 1], points[poligon[0] - 1], image, (255, 255, 255))

image.save('Output/Task7_alien.jpg')
