class car:

    def __init__(self,year,speed):
        self.year= year
        self.speed= speed
    def getSpeed(self):
        print('Maximum speed is', self.speed)
    def setSpeed(self,speed):
        self.speed= speed

BMW = car(2018, 155)
Ford= car(2016, 140)
class Sedan(car):
    def accelerate(self):
        print('137')
    def openTrunk(self):
        print('trunk has been open')
class SUV(car):
    def accelerate(self):
        print('127')

Honda= Sedan(2018,150)
BMW.getSpeed()
Honda.getSpeed()
Honda.openTrunk()
Honda.accelerate()