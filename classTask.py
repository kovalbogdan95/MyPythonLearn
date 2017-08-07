class Thing:
    pass

print(Thing)

example = Thing()

print(example)

class Thing2:
    def __init__(self):
        self.letters = 'abc'

classThing2 = Thing2()

print(classThing2.letters)

class Thing3:
    def __init__(self):
        self.letters = 'xyz'

print(Thing3().letters)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name, self.symbol, self.number)

    def __str__(self):
        return self.name + ' ' +  self.symbol + " " + str(self.number)

perEl = Element('Hydrogen', 'H', 1)

print(perEl.name, perEl.symbol, perEl.number)

propDict = {
    'name': 'Hydrogen',
    'symbol': 'H',
    'number': 1
}

hydrogen = Element(**propDict)

print(hydrogen.name, hydrogen.symbol, hydrogen.number)

hydrogen.dump()

print(hydrogen)

class Laser:
    def does(self):
        return 'disentegrate'

class Claw:
    def does(self):
        return 'cruch'

class Smartphone:
    def does(self):
        return 'ring'

class Robot(Laser, Claw, Smartphone):
    def does(self):
        return Laser().does() + ' ' + Claw().does()+ ' ' + Smartphone().does()



laser = Laser()
claw = Claw()
smartphone = Smartphone()
robot = Robot()

print(laser.does(), claw.does(), smartphone.does())

print(robot.does())