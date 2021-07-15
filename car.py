class CarClass(object) :
    def __init__(self, color, brand, speedLimit, model, seats) :
        self.color = color
        self.brand = brand
        self.speedLimit = speedLimit
        self.model = model
        self.seats = seats

    def startCar(self) :
        print("Car started")
    
    def stopCar(self) :
        print("Car stopped")

    def accelerateCar(self) :
        print("Car accelerated")

    def changeGear(self, gearType) :
        print("Gear changed to " + gearType)

    def numOfSeats(self) :
        print(self.seats)

car1 = CarClass("red", "Honda", 32422, "fsjhdf", 8) 
car1.numOfSeats()
car1.startCar()
#car1.changeGear(3)
car1.accelerateCar()
car1.stopCar()