# Инкапсуляция - это способ ограничения доступа к переменным внутри класса как на чтение, так и на изменение 

class Macbook:
    owner = None #public
    _id = None #protected
    __manufacturer = "Apple" #private
    
    def __init__(self, _id, man):
        self._id = _id
        self.__manufacturer = man

mac130 = Macbook("130", "ASSUS")

mac130.owner = "Vasily"
mac130.owner = "Nikita"

mac130._id = "150"
print(mac130._id)

mac130.__manufacturer = 100
print(mac130.__manufacturer)
print(mac130._Macbook__manufacturer)
print(dir(mac130))