import sys
import os

class Weapon:
    def __init__ (self,name,description,damage,dur,value):
        self.name = name 
        self.description = description 
        self.damage = damage
        self.dur = dur
        self.value = value

    def __repr__ (self):
        return "{}. {}. Damage: {}. Durability: {}".format(self.name, self.description,self.damage,self.dur)


class GreatSword(Weapon):
    def __init__(self):
        super().__init__(
            name = "Great sword",
            description = "A robust, heavy bladed sword, cast from steel. Inflicts servere damage",
            damage = 30,
            value = 65,
            dur = 125)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(
            name = "Dagger",
            description = "A fine choice for covert operations. Ensures a stealthy entry",
            damage = 16,
            value = 30,
            dur = 85)

class SpikedClub(Weapon):
    def __init__(self):
        super().__init__(
            name = "Spiked club",
            description = "Deadly, topheavy and wooden. Takes a share of enemy flesh after connecting a blow",
            damage = 25,
            value = 50,
            dur = 30)

class Plank(Weapon):
    def __init__(self):
        super().__init__(
            name = "Plank",
            description = "A wooden plank ripped from a crate",
            damage = 8,
            value = 0,
            dur = 5)





