#Композиция - это передача данных через аттрибуты других классов

class Engine:
    def on(self):
        print("Engine started")
        
    def off(self):
        print("Engine stopped")
        
class Stereo:
    def rock(self):
        print("I am on the highway to hell!")
        
class Car:
    __engine = Engine()#__ - использование инкапсуляции
    stereo = Stereo()
    
    def start(self):
        print("Let us ride!")
        self.stereo.rock()
        self.__engine.on()
    
    def stop(self):
        print("I am done!")
        self.__engine.off()
        
    def change_engine(self, new_engine: Engine):
        print("Installing new engine")
        self.__engine = new_engine
    
lada = Car()
#lada.engine.on()
lada.start() 
lada.stop()

engine2 = Engine()
lada.change_engine(engine2)
lada.start()      