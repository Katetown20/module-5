import math
class Point:

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def set(self):
        if self.x != self.y:
            z = int(math.sqrt((self.x**2) + (self.y**2)))
            print('Расстояние между точками Х и У =',z)
        else:
            print('координата Х = координате Y ')

    def get(self):
        print('точка имеет координаты X:',self.x, 'и Y:',self.y)

p1 = Point(7,5)
p2 = Point(7,3)

p1.set()
p1.get()

p2.set()
p2.get()



