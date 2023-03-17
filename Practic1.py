class Car:
    __wheels = 4
    
    #def get_wheels(self):
         #return self.__wheels
    
    @property
    def wheels(self):
        return self.__wheels
     
    @wheels.setter 
    def wheels(self, num):
        print("Кто-то ставит нам колёса")
        if num > 5:
            num = 4
        self.__wheels = num
     
    @wheels.deleter
    def wheels(self):
        print("Кто-то снимает наши колёса")
        self.__wheels = 0
    
car = Car()

#print(car.wheels)
#print(car.get_wheels())
#car.wheels = 10
#print(car.wheels)

del car.wheels
print(car.wheels)

car.wheels = 17
print(car.wheels)