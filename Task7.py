from Task4 import Model
from Task2 import MyImage
from Task3 import Drawer
import numpy as np

model = Model()
model.load('Test.obj')
cords = model.getCords()
poligons = model.getPoligons()

drawer = Drawer()

image = MyImage(1000, 1000)
points = np.zeros(len(cords), dtype=tuple)

k = 0
for cord in cords:
    x = int(8000 * (-cord[0]) + 500)
    y = int(8000 * (-cord[1]) + 900)
    points[k] = (x, y)
    k += 1

for poligon in poligons:
    drawer.line3(points[poligon[0] - 1], points[poligon[1] - 1], image, (255, 255, 255))
    drawer.line3(points[poligon[1] - 1], points[poligon[2] - 1], image, (255, 255, 255))
    drawer.line3(points[poligon[2] - 1], points[poligon[0] - 1], image, (255, 255, 255))

image.save('Task7.jpg')
