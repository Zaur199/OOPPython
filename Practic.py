class Purse:
    def __init__(self, valuta, name="Unknown"):
        if valuta not in ("USD", "EUR"):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name
    
    def info(self):
        print(self.__money)
    
    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany
        
    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print("Недостаточно средств!!!")
            raise ValueError("Недостаточно средств")
        self.__money = self.__money - howmany
        return howmany
    
    def __del__(self):
        print("Кошелёк удалён!!!")
    
x = Purse("USD")
y = Purse("USD", "Bill")

y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))
x.info()
y.info()
#x.top_down_balance(200)
#x.top_down_balance(20)
#x.info()
#del x
#x.__money = 200#данные инкапсулированны 
#x.info()
