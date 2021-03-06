from Task4 import Model
from Task2 import MyImage
from Task3 import Drawer
import random
import numpy as np

model = Model()

model.load('Test_alien.obj', (0, 3, 6))
model.setScale(-28, -28, 450, 700, False)
cords = model.getCords()
poligons = model.getPoligons()
points = model.getPoints()

drawer = Drawer()

image = MyImage(1000, 1000)

k = 0
last_percent = 0
print('Percent compl:')
random.seed(version=2)
for polygon in poligons:
    drawer.drawPolygon(model, polygon, image, (int(random.random()*255), int(random.random()*255), int(random.random()*255)), False)
    percent_compl = int(k / len(poligons) * 100)
    if percent_compl % 5 == 0 and last_percent != percent_compl:
        print(percent_compl)
        last_percent = percent_compl
    k += 1

image.save('Output/Task11_alien.jpg')