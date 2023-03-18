#Множественне наследование
from abc import ABC, abstractmethod
class Animal(ABC):
    #name = None
    
    @abstractmethod
    def sound(self):
        #raise NotImplementedError
        pass
        
        
class Swimming():
    name = None
    
    def run(self):
        print(self.name + " is not running!")
    
    def swim(self):
        print(self.name + " is swimming!")
        
class Running:
    name = None
    
    def run(self):
        print(self.name + " is running!")
        
class Fish(Swimming, Running):#наследование классов идёт слева направо
    def __init__(self, name):
        self.name = name
    
    #name = "Рыба"
    #def sound(self):
        #print("Буль, буль")

fish1 = Fish("Рыба1")
#fish1.sound()
fish1.swim()
fish1.run()