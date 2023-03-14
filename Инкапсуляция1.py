# Инкапсуляция - это способ ограничения доступа к переменным внутри класса как на чтение, так и на изменение 
class Macbook:
    owner = None #public
    _id = None #protected
    __manufacturer = "Apple" #private
    
    def __init__(self, _id):
        self._id = _id
        
    def __set_manf(self, man):
        self.__manufacturer = "new_man_" + man
        
    def change_man(self, man):
        print("Warning!!!")
        self.__set_manf(man)
    
    def get_man(self):
        return self.__manufacturer
    
    def set_id(self, new):
        self._id = "not_orig_" + new

mac130 = Macbook("130")

print(mac130.get_man())
print(mac130.set_id("150"))
print(mac130._id)

mac130.change_man("Asus")
print(mac130.get_man())
