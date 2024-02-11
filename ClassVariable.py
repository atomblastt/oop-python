class Hero:         # template
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputArmor, inputPower):
        self.name = inputName
        self.health = inputHealth
        self.armor = inputArmor
        self.power = inputPower
        Hero.jumlah += 1
        print(f"Hero baru {inputName} sudah di tambahkan")

hero1 = Hero("betrix", 100, 50, 200)       # object
hero2 = Hero("edora", 50, 30, 100)
hero3 = Hero(
    inputName = "ling",
    inputPower = 10,
    inputHealth = 100,
    inputArmor = 400
    )
print(f"sekarang jumlah hero menjadi {Hero.jumlah}")