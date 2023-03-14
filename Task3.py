#Конструктор класса
class Car:
    def __init__(self, name, wheels=4):
        self.name = name
        self.wheels = wheels
    def move(self): #self - ссылка объекта на мамого себя
        print("{} начинает движение на {} колёсах".format(self.name, self.wheels))

    def change(self, wheels):
        print("{} меняет колёса с {} на {}".format(self.name, self.wheels, wheels))
        self.wheels = wheels
        
toyota = Car(name="Toyota", wheels=6)
honda = Car(name="Honda")

toyota.move()
toyota.change(10)
toyota.move()

honda.move()