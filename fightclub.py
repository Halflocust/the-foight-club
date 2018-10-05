import sys
import os
import random
import pickle
import enemies
import weapons

class Player:
    total_wins = 0 

    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.health = self.max_health
        self.base_attack = 8
        self.gold = 65
        self.pots = 0
        self.weapon = ["Plank"]
        self.current_weapon = ["Plank"]
 
def set_attack():
    if PlayerIG.current_weapon == "Dagger":
        PlayerIG.base_attack = 16
    elif PlayerIG.current_weapon == "Great sword":
        PlayerIG.base_attack = 30
    elif PlayerIG.current_weapon == "Spiked club":
        PlayerIG.base_attack = 34
        

def main():
    os.system("clear")
    print ("Welcome to Foight Club\n")
    print("1) Start")
    print("2) Load")
    print("3) Exit")
    option = input(">>>  ")
    if option == "1":
        start()
    elif option == "2":
        load()
    elif option == "3":
        sys.exit()
    else:
        main()

def start():
    os.system("clear")
    print("Enter your name. Choose wisely, as a name is what defines the warior!")
    option = input(">>>  ")
    global PlayerIG
    PlayerIG = Player(option)
    start1()

def start1():
    os.system("clear")
    print ("Player Stats:")
    print ("Name: {}".format(PlayerIG.name))
    print("Total Victories: {}".format(Player.total_wins))
    print ("Health: {}/{}".format(PlayerIG.health, PlayerIG.max_health))
    print ("Attack: {}".format(PlayerIG.base_attack))
    print ("Gold: {}".format(PlayerIG.gold))
    print ("All weapons: {}".format(PlayerIG.weapon))
    print ("Current weapon: {}".format(PlayerIG.current_weapon))
    print ("Potions: {}".format(PlayerIG.pots))    
    print ()
    print ("1) Fight")
    print ("2) Shop")
    print ("3) Save")
    print ("4) Inventory")
    print ("5) Exit")
    print("6) Top scores")
    option = input(">>>  ")
    if option == "1":
        pre_fight()
    elif option == "2":
        store()
    elif option == "3":
        save()
    elif option == "4":
        inventory() 
    elif option == "5":
        main()
    elif option == "6":
        top_score()
    else:
        start1()

def pre_fight():
    global enemy
    enemy_select = random.randint(0,2)
    if enemy_select ==  0:
        enemy = enemies.Zombie()
    elif enemy_select ==  1:
        enemy = enemies.Goblin()
    if enemy_select ==  2:
        enemy = enemies.WereWolf()
    fight()        

def fight():
    os.system("clear")
    print("{} vs {}".format(PlayerIG.name, enemy.name))
    print("{}'s health: {}/{}     |||   {}'s health: {}/{}".format(PlayerIG.name,PlayerIG.health,PlayerIG.max_health,enemy.name,enemy.health, enemy.max_health))
    print("Potions: {}".format(PlayerIG.pots))
    print ("1) Attack")
    print ("2) Drink potion")
    print ("3) Flee")
    option = input(">>>  ")
    if option == "1":
        attack()
    elif option == "2":
        drink_pot()
    elif option == "3":
        run()
    else:
        fight()

def attack():
    os.system("clear")
    player_attack = random.randint(PlayerIG.base_attack/2, PlayerIG.base_attack)
    enemy_attack = random.randint(enemy.attack/2, enemy.attack)
    if player_attack == PlayerIG.base_attack/2:
        print("You miss!, its a nimble mother fucker you are fighting!")
    else:
        enemy.health -= player_attack
        print("You deal {} damage".format(player_attack))

    if enemy.health <=0:
        win()
    option = input("")
    os.system("clear")
    
    if enemy_attack == enemy.attack/2:
        print("The enemy missed!")
        dangle = input(">>>  ")
    else:
        PlayerIG.health -= enemy_attack
        print("The enemy deals {} damage".format(enemy_attack))
        dangle = input(">>>  ")
    if PlayerIG.health <=0:
        die()
    else:
        fight()


def drink_pot():
    os.system("clear")
    if PlayerIG.pots == 0:
        print("You don't have any potions")
        option = input(">>>  ")
        fight()
    else:
        PlayerIG.health += 30
        if PlayerIG.health > PlayerIG.max_health:
            PlayerIG.health = PlayerIG.max_health
            PlayerIG.pots -= 1
        print("You drank a potion")
        fight()


def run():
    os.system("clear")
    run_num = random.randint(1,3)
    if run_num == 1:
        print("You successfully ran away!")
        option = input(">>>  ")
        start1()
    else:
        print('You failed to get away!')
        option = input(">>>  ")
        os.system("clear")
    enemy_attack = random.randint(enemy.attack/2, enemy.attack)
    if enemy_attack == enemy.attack/2:
        print("The enemy missed!")
        basil = input(">>>  ")
    else:
        PlayerIG.health -= enemy_attack
        print("The enemy deals {} damage".format(enemy_attack))
        basil = input(">>>  ")
   

    if PlayerIG.health <=0:
        die()
    else:
        fight()

def inventory():
    os.system("clear")
    print("Welcome warrior named {}".format(PlayerIG.name))
    print("What do you want to do?")
    print("1) Equip different weapon")
    print("2) Back")
    option = input(">>>  ")
    if option == "1":
        equip()
    elif option == "2":
        start1()
    else:
        inventory()


def store():
    Dagger = weapons.Dagger()
    SpikedClub = weapons.SpikedClub()
    GreatSword = weapons.GreatSword()
    os.system("clear")
    print("Welcome to the shop!\n")
    print("May I interest you in any of the following items, not negotiable of course.\n")
    print("Your available gold: {}\n".format(PlayerIG.gold))
    print("1) Dagger (Value: {}. Damage: {}, Durability: {}".format(Dagger.value,Dagger.damage,Dagger.dur))
    print("2) Spiked club (Value: {}. Damage: {}, Durability: {}".format(SpikedClub.value,SpikedClub.damage,SpikedClub.dur))
    print("3) Great Sword (Value: {}. Damage: {}, Durability: {}".format(GreatSword.value,GreatSword.damage,GreatSword.dur))
    print("4) Healing potion (restores 30 health): 15 gold")
    print("5) Exit shop")
    option = input("")
    if option == "1":
        option = input("Are you sure you want to purchase the: Dagger?(y/n)")
        if option == "y":
            if PlayerIG.gold >= Dagger.value:
                os.system("clear")
                PlayerIG.gold -= Dagger.value
                PlayerIG.weapon.append(Dagger.name)   
                print("You bought a {}".format(Dagger.name))
                dongle = input(">>>  ")
                store()
            else:
                os.system("clear")
                print("You don't have enough gold")
                dongle = input(">>>  ")
                store()
        else: 
            store()

    elif option == "2":
        option = input("Are you sure you want to purchase the: Spiked clud?(y/n)")
        if option == "y":
            if PlayerIG.gold >= SpikedClub.value:
                os.system("clear")
                PlayerIG.gold -= SpikedClub.value
                PlayerIG.weapon.append(SpikedClub.name)   
                print("You bought a {}".format(SpikedClub.name))
                dongle = input(">>>  ")
                store()
            else:
                os.system("clear")
                print("You don't have enough gold")
                dongle = input(">>>  ")
                store()
        else:
            store()

    elif option == "3":
        option = input("Are you sure you want to purchase the: Great sword?(y/n)")
        if option == "y":
            if PlayerIG.gold >= GreatSword.value:
                os.system("clear")
                PlayerIG.gold -= GreatSword.value
                PlayerIG.weapon.append(GreatSword.name)   
                print("You bought a {}".format(GreatSword.name))
                dongle = input(">>>  ")
                store()
            else:
                os.system("clear")
                print("You don't have enough gold")
                dongle = input(">>>  ")
                store()
        else:
            store()
    elif option == "4":
        if PlayerIG.gold >= 15:
            PlayerIG.pots += 1
            PlayerIG.gold -= 15
            os.system("clear")
            print("You purchased a healing potion!")
            dongle = input("")
            store()
        else:
            print("Not enough gold")
            store()
    elif option == "5":
        start1()
        
    else:
        os.system('clear')
        dongle = input("That item does not exist") 
        store()


def equip():
    os.system("clear")
    print("You have the following weapons in your inventory:")
    for item in PlayerIG.weapon:
        print (item)
    print("Type b to go back")
    option = input("Type in weapon to equip  ")
    if option == PlayerIG.current_weapon:
        print("You already have that weapon equiped")
        option = input(">>>  ")
        equip()
    elif option == "b":
        inventory()
    elif option in PlayerIG.weapon:
        PlayerIG.current_weapon = option
        print("You have equiped {}!".format(PlayerIG.current_weapon))
        option = input(">>>  ")
        set_attack()
        equip()
    else: 
        print("Item, {}, not in inventory".format(option))
        equip()

def win():
    os.system("clear")
    enemy.health = enemy.max_health
    print ("You have defeated the {}".format(enemy.name))
    print ("The enemy carried {} gold. You claim it.".format(enemy.gold_gain))
    PlayerIG.gold += enemy.gold_gain
    option = input(">>>  ")
    Player.total_wins += 1
    start1()

def die():
    os.system("clear")
    print("You are dead! Game over!!! ")
    option = input(">>>  ")
    save_score()
    main()

def save():
    os.system("clear")
    with open("save-game", "wb") as f:
        pickle.dump(PlayerIG, f)
        print("Game has been saved!")
        option = input(">>>  ")
        start1()

def load():
    if os.path.exists("save-game") == True:
        os.system("clear") 
        with open("save-game", "rb") as f:
            global PlayerIG
            PlayerIG = pickle.load(f)
        print(" Loaded Save State....")
        option = input("")
    else:
        print("No saved file detected")
        option = input("")
    start1()

def save_score():
    if os.path.exists("top-score-save"):
        with open("top-score-save", "rb") as file:
            players_all_time_stats = pickle.load(file)
            players_all_time_stats.update({PlayerIG.name:Player.total_wins})
    else:
        players_all_time_stats = {PlayerIG.name:Player.total_wins}


    with open("top-score-save", "wb") as file:
        pickle.dump(players_all_time_stats,file)

    return players_all_time_stats

def top_score():
    os.system("clear")
    print(" <<< TOP SCORES >>>")
    number = 1
    scores = []
    rank = save_score()
    top_three = sorted(rank.items(),key=lambda x: -x[1])[:3]
    for item in top_three:
        print("#{}  {}: {}".format(number,item[0],item[1]))
        number += 1

    print("Hit any key to return")
    choice = input()
    start1()

    

# def Room1():    
#     os.system("clear")
#     print ("""I don't know what drove you to insanity,{}. Surely you are a demented soul or exeedingly desperate to have come here. By entering you have resigned to death! No person has left this place. """.format(PlayerIG.name))
#     print("Every sight and smell is a reminder of the torment that the walls have witnessed.")



main()