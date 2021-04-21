from Task4 import Model
from Task2 import MyImage
from Task3 import Drawer
import math
import random
import numpy as np

model = Model()

model.load('Test_alien.obj', (0, 3, 6))
model.setScale(-28, -28, 450, 700, False)
#model.load('Test_rabbit.obj', (0, 3, 6))
#model.setScale(-8000, -8000, 500, 900, False)
poligons = model.getPoligons()
cos_lights = model.getCos_light()
points = model.getPoints()
apex_normals = model.getApex_normals()

drawer = Drawer()

N = 1000
M = 1000

image = MyImage(N, M)

k = 0
last_percent = 0
print('Percent compl:')
for polygon in poligons:
    if cos_lights[k] < 0:
        drawer.drawPolygon_Guro(model, polygon, apex_normals[k], image)
    percent_compl = int(k / len(poligons) * 100)
    if percent_compl % 5 == 0 and last_percent != percent_compl:
        print(percent_compl)
        last_percent = percent_compl
    k += 1

image.save('Output/Task18_alien.jpg')
#image.save('Output/Task18_rabbit.jpg')