class Hero:         # template
    def __init__(self, inputName, inputHealth, inputArmor, inputPower):
        self.name = inputName
        self.health = inputHealth
        self.armor = inputArmor
        self.power = inputPower

hero1 = Hero("betrix", 100, 50, 200)       # object
hero2 = Hero("edora", 50, 30, 100)
hero3 = Hero(
    inputName = "ling",
    inputPower = 10,
    inputHealth = 100,
    inputArmor = 400
    )

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)