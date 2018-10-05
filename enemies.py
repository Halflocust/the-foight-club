class Enemy():
    def __init__(self,name,attack,health,max_health,gold_gain):
        self.name = name
        self.attack = attack
        self.health = health
        self.max_health = max_health
        self.gold_gain = gold_gain


class WereWolf(Enemy):
    def __init__ (self):
        super(). __init__(
            name = "Werewolf",
            attack = 16,
            max_health = 30,
            health = 30,
            gold_gain = 20
        )

class Goblin(Enemy):
    def __init__ (self):
        super(). __init__(
            name = "Goblin",
            attack = 16,
            max_health = 20,
            health = 20,
            gold_gain = 10
        )

class Zombie(Enemy):
    def __init__ (self):
        super(). __init__(
            name = "Zombie",
            attack = 10,
            max_health = 40,
            health = 40,
            gold_gain = 10
        )


class MrPeanutbutter(Enemy):
    def __init__ (self):
        super(). __init__(
            name = "Mr Peanutbutter",
            attack = 8,
            max_health = 25,
            health = 25,
            gold_gain = 5
        )

class Greg(Enemy):
    def __init__ (self):
        super(). __init__(
            name = "Greg",
            attack = 28,
            max_health = 20,
            health = 20,
            gold_gain = 10
        )





