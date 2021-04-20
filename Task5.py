from Task4 import Model
from Task2 import MyImage

model = Model()
# model.load('Test_rabbit.obj', (0,3,6))
# cords = model.getCords()
#
# image = MyImage(1000, 1000)
#
# for cord in cords:
#     x = int(8000 * (-cord[0]) + 500)
#     y = int(8000 * (-cord[1]) + 900)
#     image.set(x, y, (255, 255, 255))
#
# image.save('Output/Task5_rabbit.jpg')
#
model.load('Test_alien.obj', (0, 3, 6), -28, 450, -28, 700, (0, 0, 1))
cords = model.getCords()

image = MyImage(1000, 1000)

for cord in cords:
    x = int(-28*cord[0] + 450)
    y = int(-28*cord[1] + 700)
    image.set(x, y, (255, 255, 255))

image.save('Output/Task5_alien.jpg')
