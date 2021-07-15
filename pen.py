class PenClass(object) :
    def __init__(self, color, type, brand) :
        self.color =  color
        self.type = type
        self.brand = brand

    def write(self) :
        print("Writing")

    def empty(self) :
        print("Refilling of ink required!")

pen1 = PenClass("blue", "click", "shreya") 
pen1.empty()