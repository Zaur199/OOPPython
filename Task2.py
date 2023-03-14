#Атрибуты - это переменные; методы - это функции
class Car:
    wheels = 4
    def move(self): #self - ссылка объекта на мамого себя
        print("Начинаем движение на {} колёсах".format(self.wheels))

    def change(self, wheels):
        print("Меняю колёса с {} на {}".format(self.wheels, wheels))
        self.wheels = wheels
    
toyota = Car()
honda = Car()

print(toyota.wheels)
print(honda.wheels)

toyota.change(3)

print(toyota.wheels)
print(honda.wheels)

