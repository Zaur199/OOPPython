#Волшебные методы классов

class Car:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def __str__(self):
        return "{}: {} pw".format(self.name, self.power)
    
    def __repr__(self):
        return "{}:{}".format(self.name, self.power)

    def __call__(self, *args, **kwargs):
        #return "{} is calling".format(self.name)
        print("{} is calling".format(self.name))
        
    def __add__(self, other):
        return Car(self.name + other.name, self.power + other.power)    
        
toyota = Car("Toyota", 200)
honda = Car("Honda", 150)

new_car = toyota + honda
print([new_car, new_car])
#print(toyota + honda)

#print(toyota)

#garage = [toyota, toyota, toyota]
#print(garage)

#toyota()#вызываем как функцию

