from Task4 import Model
from Task2 import MyImage

model = Model()

model.load('Test_alien.obj', (0, 3, 6))
model.setScale(-28, -28, 450, 700, False)
points = model.getPoints()

image = MyImage(1000, 1000)

for point in points:
    image.set(point[0], point[1], (255, 255, 255))

image.save('Output/Task5_alien.jpg')
