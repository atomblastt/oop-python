class Hero:         # template
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputArmor, inputPower):
        self.name = inputName
        self.health = inputHealth
        self.armor = inputArmor
        self.power = inputPower
        Hero.jumlah += 1
        print(f"Hero baru {inputName} sudah di tambahkan")

    # void function, tanpa return
    def siapaIni(self):
        print(f"Namaku adalah {self.name}")

    # void function, dengan return
    def healthUp(self, up):
        return self.health + up

    # void function, dengan return
    def getHealt(self):
        return self.health

hero1 = Hero("betrix", 100, 50, 200)       # object
hero1.siapaIni()
print(hero1.healthUp(10))
print(f"Sebelumnya memilki Health {hero1.getHealt()}, dan sekarang di up menjadi {hero1.healthUp(10)}")