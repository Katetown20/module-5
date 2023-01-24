class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def set(self, x = None, y = None):
        if x==y:
            x_y = x**y
            print('х в степени у = ',x_y)
        else:
            print('координата Х: ',x, 'координата Y: ', y)

    def get(self, x = None, y = None):
        print('точка имеет координаты: ',x,y)

p1 = Point()
p2 = Point()

p1.set(3,4)
p1.set(3,3)

p2.get(7,9)



