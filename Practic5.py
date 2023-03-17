#Абстрактные методы и модуль АВС
from abc import ABC, abstractmethod
class Figure(ABC):
    
    #@property
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def name(self):
        pass

class Circle(Figure):
    
    #@property
    def area(self):
        pass
    
    def name(self):
        pass

#f = Figure()
c = Circle()