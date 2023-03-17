class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
        self.cache = {}
        
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if self.cache != {}:
            print("Drop cache")
            self.cache = {}
        self._celsius = value
        
    @property
    def kelvin(self):
        if "kelvin" not in self.cache.keys():
            print("Calculating kelvin")
            self.cache["kelvin"] = self._celsius - 273.15
        return self.cache["kelvin"]
            
    
    @property
    def farenheight(self):
        if "farenheight" not in self.cache.keys():
            print("Calculating farenheight")
            self.cache["farenheight"] = self._celsius * 9 / 5 + 32
        return self.cache["farenheight"]
    
t = Temperature(25)

print("=====First call")
print(t.kelvin)
print(t.farenheight)

print("=====Second call")
print(t.kelvin)
print(t.farenheight)


print("After change")
t.celsius = 30
print(t.kelvin)
print(t.farenheight)