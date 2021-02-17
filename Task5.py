from Task4 import Model
from Task2 import MyImage

model = Model()
model.load('Test.obj')
cords = model.getCords()

image = MyImage(1000, 1000)

for cord in cords:
    x = int(8000 * (-cord[0]) + 500)
    y = int(8000 * (-cord[1]) + 900)
    image.set(x, y, (255, 255, 255))

print(len(cords))

image.save('Task5.jpg')
