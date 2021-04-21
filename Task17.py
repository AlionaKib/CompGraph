from Task4 import Model
from Task2 import MyImage
from Task3 import Drawer
import random
import numpy as np

model = Model()

model.load('Test_alien.obj', (0, 3, 6))
model.setScale(-28, -28, 450, 700, False)
poligons = model.getPoligons()
cos_lights = model.getCos_light()

model.rotate(0, 90, 0)

drawer = Drawer()

N = 1000
M = 1000

image = MyImage(N, M)

k = 0
last_percent = 0
print('Percent compl:')
for polygon in poligons:
    if cos_lights[k] < 0:
        drawer.drawPolygon(model, polygon, image, (int(-255 * cos_lights[k]), int(-255 * cos_lights[k]), int(-255 * cos_lights[k])), True)
    percent_compl = int(k / len(poligons) * 100)
    if percent_compl % 5 == 0 and last_percent != percent_compl:
        print(percent_compl)
        last_percent = percent_compl
    k += 1

image.save('Output/Task17_alien.jpg')