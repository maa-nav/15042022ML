class Car:
    count = 0
    d_price = 0.2
    def __init__(self,brand,engine,price):
##        self.color = color
        self.brand = brand
##        self.model = model
        self.engine = engine
        self.price = price
        Car.count+=1
        
    def discount(self):
        self.price = (self.price * (1-self.d_price))
        
    def drive(self):
        print('The ' ,self.brand,'has started')
    def lighton(self):
        print('lights On')

class sedan(Car):
    d_price = 0.30



