#parent class
class Car:
    def start(self):
        print("Starting...")

    def stop(self):
        print("Stopping")    

#child

class electricCar(Car):
    def charging(self):
        print("Charging")

class petrolCar(Car):
    def fueling(Self):
        print("Fueling") 

tvs1 = electricCar()

tvs1.start()
tvs1.stop()
tvs1.charging()

i20 = petrolCar()

i20.start()
i20.stop()
i20.fueling()
