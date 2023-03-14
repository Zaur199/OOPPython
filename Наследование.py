class Moving:
    def move(self): #self - ссылка объекта на мамого себя
        print("{} движется на колёсах".format(self.name))
        #name = None("заглушка")

class Vehicle:
    def __init__(self, name, wheels, color="white"):
        self.name = "Name"
        self.wheels = wheels
        self.color = color
        
    def change(self, wheels):
        print("{} меняет колёса с {} на {}".format(self.name, self.wheels, wheels))
        self.wheels = wheels
        
    def stop(self):
        print("{} остановился".format(self.name))
    
class Car(Vehicle, Moving):
    pass
        
class Bike(Vehicle):
    pass

class SuperBike(Bike):
    pass
        
toyota = Car(name="Toyota", wheels=6)
honda = Car(name="Honda", wheels=4)
kawasaki = Bike(name="Kawasaki", wheels=2)
ducati = SuperBike(name="Ducati", wheels=2)

toyota.move()
toyota.change(10)
toyota.move()
honda.move()
kawasaki.stop()

#issubclass - проверяет является ли метод подклассом другого класса
print(issubclass(SuperBike, Bike))
print(issubclass(SuperBike, Vehicle))

#isinstance - показывает, относится ли объект к определённому классу
print(isinstance(ducati, SuperBike))