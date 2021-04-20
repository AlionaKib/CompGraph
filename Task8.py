from Task4 import Model
from Task2 import MyImage
from Task3 import Drawer
import numpy as np

model = Model()

model.load('Test_alien.obj', (0,3,6), -28, 450, -28, 700)
cords = model.getCords()
poligons = model.getPoligons()
points = model.getPoints()

bar_cords = model.getBaricentCords(points[100], poligons[8])

print(bar_cords)
print(bar_cords[0]+bar_cords[1]+bar_cords[2])