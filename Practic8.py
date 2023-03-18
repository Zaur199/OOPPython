#Метод Super()

class Rectangle:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        
    def area(self):
        return self.w * self.h

class Square(Rectangle):
    def __init__(self, s):
        #Rectangle.__init__(self, s, s)
        super().__init__(h=s, w=s)

class Cube(Square):
    #def __init__(self, s):
        #super().__init__(s)
        #self.d = s(ввели дополнительную переменную)
        
    def area(self):
        return super().area() * 6
    
    def volume(self):
        return self.h ** 3

sq = Square(10)
print(sq.area())

cu = Cube(10)
print(cu.area())
print(cu.volume())