#Полиморфизм - это возможность изменять поведение в классах наследниках

class Car:
    wheels = 4
    
    def drive(self):
        print("Engine soung")
    
    def start(self):
        print("Car started")
    
class LadaGranta(Car):
    pass

class Bugatti(Car):
    def start(self):
        print("My SuperCar started!")#переопределяем метод в классах - наследниках
        
    def drive(self):
        print("MySuper Car is DRIVING")   

lada = LadaGranta()
bugatti = Bugatti()

lada.start()
lada.drive()

bugatti.start()
bugatti.drive()