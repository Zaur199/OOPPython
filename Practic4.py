# Декоратор classmethod

import random


class Car:
    __COUNT = 1
    #__BRAND = "Toyota"

    def __init__(self, color, price):
        self.color = color
        self.price = price
        self._up_counter()#для срабатывания счётчика при каждом вызове
        
    @classmethod
    def _up_counter(cls):
        print("Создали новую тачку")
        if cls.__COUNT > 5:
            raise Exception("Больше никаких машин")
        print(cls.__COUNT)
        cls.__COUNT += 1

    @property
    def count(self):
        return self.__COUNT
    
    #@property
    #def brand(self):
        #return self.__BRAND

    #@classmethod
    #def set_brand(cls, name):
        #cls.__BRAND = name

    @classmethod
    def random_car(cls):
        return cls(color=random.choice(["red", "yellow", "white"]), price=random.randint(9000, 999999))

    # def set_brand(self, name):
        #Car.__BRAND = name

# class OneCar(Car):
    # pass


car = Car.random_car()
car1 = Car.random_car()
car2 = Car.random_car()
car3 = Car.random_car()
car4 = Car.random_car()
car5 = Car.random_car()

print(car.count)

#print(car1.brand)
#print(car1.color)
#print(car2.color)
#print(car3.color)
#print(car3.price)
#car = OneCar("fa", 343)
#car2 = OneCar("farer", 3434)

# car.set_brand("BMW")

# print(car2.brand)
# print(car.brand)

#car3 = Car("dsf", 435)
# print(car3.brand)
