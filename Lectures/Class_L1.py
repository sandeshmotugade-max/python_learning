
class Car :

    def __init__(self,model,color,wheel,seat):
        self.model = model
        self.color = color
        self.wheel = wheel
        self.seat  = seat
        print("Initialised...",self.model,self.color,self.seat,self.wheel)

class ElectricCar(Car):

    def __init__(self, model, color, wheel, seat):
        self.model = model
        self.color = color
        self.wheel = wheel
        self.seat  = seat
        print("Initialised Electric Car....",self.model,self.color,self.seat,self.wheel)

i20 = Car("i20","white",4,4)
swift = Car("swift","black",4,4)
TVS = ElectricCar("TVS","Brown",2,2)
              

