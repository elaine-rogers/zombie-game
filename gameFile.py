import random
import math

#-------------------------------------------------------------------------------#
#                               Global Variables                                #
#-------------------------------------------------------------------------------#

visitedBase = lootedBaseKitchen = lootedBaseLivingRoom = lootedBaseBedroom = lootedBaseBathroom = leftTrailer = lootedTrailerCabinets = lootedTrailerLoft = lootedHospitalBreakRoom = lootedPoliceLockerRoom = lootedPoliceArmory = lootedHospitalReceptionRooom = False
lootedTrailerBathroom = lootedPlaygroundMonkeyGym = lootedPlaygroundSandbox = leftSuburbs = lootedSuburbsKitchen = lootedSuburbsLivingRoom = lootedSuburbsMasterBedroom = lootedSuburbsBedroom = lootedSuburbsBathroom = suburbsBathroomIndex = False
trailerCounter = suburbsCounter = 0
kitchen = ([] for i in range(16))
livingRoom = ([] for i in range(16))
bedroom =  ([] for i in range(16))
bathroom =  ([] for i in range(16))
trailerCabinets = ([] for i in range(16))
trailerBedroom = ([] for i in range(16))
trailerBathroom = ([] for i in range(16))
monkeyGym = ([] for i in range(16))
sandbox = ([] for i in range(16))
suburbsKitchen = ([] for i in range(16))
suburbsLivingRoom = ([] for i in range(16))
suburbsMasterBedroom = ([] for i in range(16)) 
suburbsBedroom = ([] for i in range(16))
lootedBedroomCounter = ([] for i in range(16)) 
lootedBathroomCounter = ([] for i in range(16))
lockerRoom = ([] for i in range(16))
suburbsBedroomCounter = random.randint(1, 4)
suburbsBathroomCounter = random.randint(1, 3)
inventory = {}
equippedArmor = {}
health = 500
hygiene = hunger = sleep = 100
zombieNumber = random.randint(200, 350)
equippedWeapon = None
random.seed()

class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

#-------------------------------------------------------------------------------#
#                               Inventory Maker                                 #
#-------------------------------------------------------------------------------#

#inventory = {item: {quantity: number}}

#grab something and put it into the inventory
def putInventory(item, quant): 
    global inventory
    if item.name in inventory:
        inventory[item.name].quantity += quant
    else:
        item.quantity = quant
        inventory[item.name] = item

#remove something from the inventory
def removeInventory(item, quant): 
        global inventory
        if inventory[item.name].quantity <= quant:
             inventory.pop(item)
        else:
            inventory[item.name].quantity -= quant

#equips something from the inventory onto the player
def equipItem():
    global inventory, equippedArmor, equippedWeapon
    try:
        itemIndex = int(input(f"Which item do you want to equip?"))
    except ValueError:
        print("You have no items to equip.")
    if itemIndex < len(inventory):
        keys = list(inventory.keys())
        itemKey = keys[itemIndex]
        if inventory[itemKey].type == "Weapon" and not equippedWeapon:
            print(f"You have equipped {inventory[itemKey].name}")
            equippedWeapon = inventory[itemKey]
        if inventory[itemKey].type == "Armor" and inventory[itemKey] not in equippedArmor:
            print(f"{bcolors.FAIL}DEBUG ARMOR{bcolors.ENDC}")
            print(f"You have equipped {inventory[itemKey]}")
            equippedArmor.update({inventory[itemKey].name: inventory[itemKey]})
        else:
            print(f"You cannot equip {inventory[itemKey].name}")

#loots the location and adds it to the inventory
def looting(lootTable):
    global inventory
    if len(lootTable) == 0:
            print("There is nothing to take")
            return 0
    for loot in lootTable:
        print(loot.name)
    print("1. Take all")
    print("2. Take specific item")
    print("3. Take nothing")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        for loot in lootTable:
            putInventory(loot, 1)
        lootTable.clear()
        return 0
    if desination == "2":
        for i in range(len(lootTable)):
            print(f"{i+1}. {lootTable[i].name}")
        itemIndex = int(input(f"{bcolors.WARNING}Which item do you want to take?{bcolors.ENDC}")) - 1
        if itemIndex < len(lootTable):
            putInventory(lootTable[itemIndex], 1)
            lootTable.pop(itemIndex)
            return 0
    elif desination == "3":
        print(f"{bcolors.OKBLUE}You take nothing.{bcolors.ENDC}")
        return 1

#-------------------------------------------------------------------------------#
#                               Loot Maker                                      #
#-------------------------------------------------------------------------------#

class Item:
    def __init__(self, name, itemType, damage, damageType, protection):
        self.name = name
        self.type = itemType
        self.damage = damage
        self.damageType = damageType
        self.protection = protection
        self.quantity = 1

#name, item type, damage, damage type, protection
def lootFood(randNum):
    if randNum < 0.5:
        return Item("Canned Food", "Food", "None", 0, 0)
    if randNum < 0.8:
        return Item("Bread", "Food", "None", 0, 0)
    if randNum < 0.9:
        return Item("Meat", "Food", "None", 0, 0)
    return Item("Cake", "Food", "None", 0, 0)
        
#loot for class Kitchen Utensil 2 means weapons
def lootKitchenUtensil(randNum):
    if randNum < 0.5:
        return Item("Rolling Pin", "Weapon", "Blunt", 5, 0)
    if randNum < 0.8:
        return Item("Pan", "Weapon", "Blunt", 10, 0)
    if randNum < 0.9:
        return Item("Knife", "Weapon", "Slash", 20, 0)
    return Item("Pipe Wrench", "Weapon", "Blunt", 30, 0)
    
#loot for class Electronics. 3 means electronics
def lootElectronics(randNum):
    if randNum < 0.5:
        return Item("Radio", "Electronics", "None", 0, 0)
    if randNum < 0.8:
        return Item("Laptop", "Electronics", "None", 0, 0)
    return Item("Phone", "Electronics", "None", 0, 0)

#loot for class sheets. 4 means sheets
def lootSheets(randNum):
    if randNum < 0.7:
        return Item("Pillow", "Sheets", "None", 0, 0)
    return Item("Blanket", "Sheets", "None", 0, 0)

#loot for class cleaning supplies. 5 means cleaning supplies
def lootCleaningSupplies(randNum):
    if randNum < 0.5:
        return Item("Soap", "Cleaning Supplies", "None", 0, 0)
    if randNum < 0.8:
        return Item("Cleaning Spray", "None", "Cleaning Supplies", 0, 0)
    return Item("Bleach", "Cleaning Supplies", "None", 0, 0)

#loot for class medical supplies. 6 means medical supplies
def lootMedicalSupplies(randNum):
    if randNum < 0.8:
        return Item("Bandages", "Medical Supplies", "None", 0, 0)
    if randNum < 0.5:
        return Item("Painkillers", "Medical Supplies", "None", 0, 0)
    return Item("Antibiotics", "Medical Supplies", "None", 0, 0)

#loot for class weapons. 2 means weapons
def lootWeapons(randNum):
    if randNum < 0.5:
        return Item("Baseball Bat", "Weapon", "Blunt", 25, 0)
    if randNum < 0.8:
        return Item("Crowbar", "Weapon", "Blunt", 35, 0)
    return Item("Machete", "Weapon", "Slash", 50, 0)

#loot for class shovels. Offshoot of weapons
def lootShovels(randNum):
    if randNum < 0.5:
        return Item("Spade", "Weapon", "Slash", 10, 0)
    if randNum < 0.8:
        return Item("Garden Shovel", "Weapon", "Blunt", 20, 0)
    return Item("Snow Shovel", "Weapon", "Blunt", 20, 0)

#loot for toys. 8 means toys
def lootToys(randNum):
    if randNum < 0.3:
        return Item("Doll", "Toy", "None", 0, 0)
    if randNum < 0.5:
        return Item("Toy Car", "Toy", "None", 0, 0)
    if randNum < 0.8:
        return Item("Rubiks Cube", "Toy", "None", 0, 0)
    return Item("Baseball Bat", "Weapon", "Blunt", 25, 0)

#loot for backpacks. 9 means backpacks
def lootBackpacks(randNum):
    if randNum < 0.5:
        return Item("School Backpack", "Backpack", "None", 0, 0)
    if randNum < 0.8:
        return Item("Hiking Backpack", "Backpack", "None", 0, 0)
    return Item("Duffle Bag", "Backpack", "None", 0, 0)

#loot for stationary. 10 means stationary
def lootStationary(randNum):
    if randNum < 0.6:
        return Item("Notebook", "Stationary", "None", 0, 0)
    if randNum < 0.7:
        return Item("Pencil", "Stationary", "None", 0, 0)
    if randNum < 0.8:
        return Item("Black Pen", "Stationary", "None", 0, 0)
    if randNum < 0.9:
        return Item("Blue Pen", "Stationary", "None", 0, 0)
    return Item("Red Pen", "Stationary", "None", 0, 0)

#loot for guns. Subsection of weapons
def lootGuns(randNum):
    if randNum < 0.7:
        return Item("Pistol", "Weapon", "Shot", 60, 0)
    if randNum < 0.9:
        return Item("Rifle", "Weapon", "Shot", 90, 0)
    return Item("Shotgun", "Weapon", "Shot", 120, 0)

def lootArmor(randNum):
    if randNum < 0.2:
        return Item("Shin and Knee Gaurds", "Armor", "None", 0, 10)
    if randNum < 0.4:
        return Item("Arm Gaurds", "Armor", "None", 0, 10)
    if randNum < 0.6:
        return Item("Bullet Proof Vest", "Armor", "None", 0, 30)
    if randNum < 0.8:
        return Item("Riot Helmet", "Armor", "None", 0, 20)
    return Item("Riot Shield", "Armor", "None", 0, 20)      
            
#Loot table for different areas
def lootTable(area):
    randNum = random.random()
    randItem = random.random()
    if area == "kitchen":
        if randNum < 0.1:
            return lootKitchenUtensil(randItem)
        return lootFood(randItem)
    elif area == "baseLivingRoom":
        return lootElectronics(randItem)
    elif area == "bedroom":
        if(randNum < 0.1):
            return lootElectronics(randItem)
        return lootSheets(randItem)
    elif area == "bathroom":
        if randNum < 0.7:
            return lootCleaningSupplies(randItem)
        return lootMedicalSupplies(randItem)
    elif area == "trailerInsideCabinets":
        if randNum < 0.3:
            return lootFood(randItem)
        if randNum < 0.6:
            return lootKitchenUtensil(randItem)
        if randNum < 0.8:
            return lootCleaningSupplies(randItem)
        if randNum < 0.9:
            return lootMedicalSupplies(randItem)
        return lootWeapons(randItem)
    elif area == "playgroundMonkeyGym":
        if randNum < 0.9:
            return lootToys(randItem)
        return lootBackpacks(randItem)
    elif area == "playgroundSandbox":
        if randNum < 0.8:
            return lootToys(randItem)
        if randNum < 0.9:
            return lootShovels(randItem)
        return lootBackpacks(randItem)
    elif area == "trails":
        if randNum < 0.05:
            return lootFood(randItem)
        if randNum < 0.15:
            return lootKitchenUtensil(randItem)
        if randNum < 0.25:
            return lootElectronics(randItem)
        if randNum < 0.35:
            return lootSheets(randItem)
        if randNum < 0.45:
            return lootCleaningSupplies(randItem)
        if randNum < 0.55:
            return lootMedicalSupplies(randItem)
        if randNum < 0.65:
            return lootWeapons(randItem)
        if randNum < 0.75:
            return lootToys(randItem)
        if randNum < 0.85:
            return lootBackpacks(randItem)
        return lootStationary(randItem)
    elif area == "reception":
        if randNum < 0.9:
            return lootStationary(randItem)
        return lootElectronics(randItem)
    elif area == "medicalRoom":
        return lootMedicalSupplies(randItem)
    elif area == "breakRoom":
        if randNum < 0.5:
            return lootFood(randItem)
        if randNum < 0.8:
            return lootElectronics(randItem)
        return lootStationary(randItem)
    elif area == "apartment":
        if randNum < 0.05:
            return lootFood(randItem)
        if randNum < 0.15:
            return lootKitchenUtensil(randItem)
        if randNum < 0.25:
            return lootElectronics(randItem)
        if randNum < 0.35:
            return lootSheets(randItem)
        if randNum < 0.45:
            return lootCleaningSupplies(randItem)
        if randNum < 0.55:
            return lootMedicalSupplies(randItem)
        if randNum < 0.65:
            return lootWeapons(randItem)
        if randNum < 0.75:
            return lootToys(randItem)
        if randNum < 0.85:
            return lootShovels(randItem)
        if randNum < 0.95:
            return lootBackpacks(randItem)
        return lootStationary(randItem)
    elif area == "policeLockerRoom":
        if randNum < 0.3:
            return lootFood(randItem)
        if randNum < 0.6:
            return lootGuns(randItem)
        return lootArmor(randItem)
    elif area == "policeArmory":
        if randNum < 0.5:
            return lootGuns(randItem)
        return lootArmor(randItem)

#-------------------------------------------------------------------------------#
#                               Zombie Maker                                    #
#-------------------------------------------------------------------------------#
def Zombie(difficulty):
    global zombieNumber
    if difficulty == "easy":
        health = random.randint(50, 75)
        damage = 10
    if difficulty == "medium":
        health = random.randint(75, 125)
        damage = 30
    if difficulty == "hard":
        health = random.randint(125, 200)
        damage = 50
    zombieNumber -= 1
    return {"health": health, "damage": damage}

def ZombieGroup(difficulty):
    global zombieNumber
    zombieGroup = []
    if difficulty == "easy":
        for i in range(random.randint(1, 2)):
            if zombieNumber > 0:
                zombieGroup.append(Zombie(difficulty))
                zombieNumber -= 1
    elif difficulty == "medium":
        for i in range(random.randint(1, 4)):
            if zombieNumber > 0:
                zombieGroup.append(Zombie(difficulty))
                zombieNumber -= 1
    elif difficulty == "hard":
        for i in range(random.randint(1, 7)):
            if zombieNumber > 0:
                zombieGroup.append(Zombie(difficulty))
                zombieNumber -= 1
    return zombieGroup

#-------------------------------------------------------------------------------#
#                               Fighting Loop                                   #
#-------------------------------------------------------------------------------#

def useWeapon(equippedWeapon):
    if not equippedWeapon:
        print("You punch the Zombie")
        damage = 5 - random.randint(0, 2)
        print(f"You do {damage} damage")
        return damage
    if equippedWeapon.damageType == "Slash":
        print("You slash at the Zombie")
        damage = equippedWeapon.damage - random.randint(0, (math.floor(equippedWeapon.damage / 2)))
        print(f"You do {damage} damage")
        return damage
    if equippedWeapon.damageType == "Blunt":
        print("You bludgeon the Zombie")
        damage = equippedWeapon.damage - random.randint(0, (math.floor(equippedWeapon.damage / 2)))
        print(f"You do {damage} damage")
        return damage
    else:
        print("Something went wrong!!!!")
        return 9999

def damage(difficulty):
    if difficulty == "easy":
        return random.randint(1, 20)
    if difficulty == "medium":
        return random.randint(1, 40)
    if difficulty == "hard":
        return random.randint(20, 60)

def fightingMiniGame(difficulty, zombieGroup):
    global health, zombieNumber, equippedWeapon, equippedArmor
    while (health > 0 and zombieGroup):
        printDamage = []
        block = 0
        for i in equippedArmor:
            block += equippedArmor[i].protection
        print(f"You have {health} health left.")
        print(f"There are {len(zombieGroup)} zombies left.")
        for i in range(len(zombieGroup)):
            print(f"{i+1}. Zombie Health: {zombieGroup[i]["health"]}")
            
        print(f"-----------------------------")
        print("1. Fight")
        print("2. Escape")
        print("3. Block")

        for i in zombieGroup:
            printDamage.append(damage(difficulty))
        
        command = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if command == "1":
            for i in range(len(zombieGroup)):
                print(f"{i+1}. Zombie Health: {zombieGroup[i]["health"]}")
            try:
                command = int(input(f"{bcolors.WARNING}Which zombie do you want to attack?{bcolors.ENDC}")) - 1
            except ValueError:
                print("No Zombie Selected.")
                return
            zombieGroup[command]["health"] -= useWeapon(equippedWeapon)
            print(f"Zombie has {zombieGroup[command]["health"]}")
            if zombieGroup[command]["health"] <= 0:
                zombieNumber -= 1
                zombieGroup.pop(command)
        elif command == "2":
            escape = True
            for i in range(len(zombieGroup)):
                if random.random() > 0.8:
                    escape = False
            if escape == True:
                print("You manage to escape.")
                zombieGroup.clear()
                return
            else:
                print("You can't escape.")
        elif command == "3":
            print(printDamage)
            for i in range(len(printDamage)):
                printDamage[i] = printDamage[i] / 2
        else:
            print("You do nothing")
        for i in range(len(printDamage)):
            printDamage[i] -= block
            if printDamage[i] < 0:
                printDamage[i] = 0
            health -= printDamage[i]
            print(f"You take {printDamage[i]} damage")

#-------------------------------------------------------------------------------#
#                               Location Maker                                  #
#-------------------------------------------------------------------------------#
class Location:
    def base():
        global visitedBase
        if not visitedBase:
            print(f"{bcolors.OKBLUE}You are in a small cabin on the outskirts of town.{bcolors.ENDC}")
            visitedBase = True
        print(f"{bcolors.OKBLUE}You are at your base.{bcolors.ENDC}")
        print("1. Leave the base")
        print("2. Visit Kitchen")
        print("3. Visit Living Room")
        print("4. Visit Bedroom")
        print("5. Visit Bathroom")
        desination = (input(f"{bcolors.WARNING}Where do you want to go?{bcolors.ENDC}"))
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the base.{bcolors.ENDC}")
            return "outsideBase"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You enter the kitchen.{bcolors.ENDC}")
            return "baseKitchen"
        elif desination == "3":
            print(f"{bcolors.OKBLUE}You enter the living room.{bcolors.ENDC}")
            return "baseLivingRoom"
        elif desination == "4":
            print(f"{bcolors.OKBLUE}You enter the bedroom.{bcolors.ENDC}")
            return "baseBedroom"
        elif desination == "5":
            print(f"{bcolors.OKBLUE}You enter the bathroom.{bcolors.ENDC}")
            return "baseBathroom"
        return "base"
        
    def outsideBase():
        if random.random() < 0.1:
            fightingMiniGame("easy", ZombieGroup("easy"))
        print(f"{bcolors.OKBLUE}You are outside the base.{bcolors.ENDC}")
        print("1. Go back to the base")
        print("2. Go to Trailer Park")
        print("3. Go to Park")
        destination = input(f"{bcolors.WARNING}Where do you want to go?{bcolors.ENDC}")
        if destination == "1":
            print(f"{bcolors.OKBLUE}You go back to the base.{bcolors.ENDC}")
            return "base"
        elif destination == "2":
            print(f"{bcolors.OKBLUE}You go to the Trailer Park.{bcolors.ENDC}")
            return "trailerPark"
        elif destination == "3":
            print(f"{bcolors.OKBLUE}You go to the park.{bcolors.ENDC}")
            return "park"
        return "outsideBase"

    def baseKitchen():
        global inventory, lootedBaseKitchen
        kitchen = []
        print(f"{bcolors.OKBLUE}You are in the kitchen.{bcolors.ENDC}")
        print("1. Go back to the hallway")
        print("2. Search the kitchen")
        print("3. Cook something")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the kitchen.{bcolors.ENDC}")
            return "base"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You find:{bcolors.ENDC}")
            if not lootedBaseKitchen:
                lootedBaseKitchen = True
                kitchen = [lootTable("kitchen"), lootTable("kitchen"), lootTable("kitchen")]
            looting(kitchen)
            return "baseKitchen"
        elif desination == "3":
            print(f"{bcolors.FAIL} FINISH COOKING LATER {bcolors.ENDC}")
            return "baseKitchen"
        return "baseKitchen"
        
    def baseLivingRoom():
        global inventory, lootedBaseLivingRoom
        print(f"{bcolors.OKBLUE}You are in the living room.{bcolors.ENDC}")
        print("1. Go back to the hallway")
        print("2. Search the living room")
        print("3. Watch TV")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the living room.{bcolors.ENDC}")
            return "base"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You find:{bcolors.ENDC}")
            if not lootedBaseLivingRoom:
                lootedBaseLivingRoom = True
                livingRoom = [lootTable("baseLivingRoom"), lootTable("baseLivingRoom")]
            looting(livingRoom)
            return "baseLivingRoom"
        elif desination == "3":
            print(f"{bcolors.FAIL} FINISH WATCHING TV LATER {bcolors.ENDC}")
            return "baseLivingRoom"
        return "baseLivingRoom"
        
    def baseBedroom():
        global lootedBaseBedroom
        print(f"{bcolors.OKBLUE}You are in the bedroom.{bcolors.ENDC}")
        print("1. Go back to the hallway")
        print("2. Search the bedroom")
        print("3. Sleep")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the bedroom.{bcolors.ENDC}")
            return "base"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You find:{bcolors.ENDC}")
            if not lootedBaseBedroom:
                lootedBaseBedroom = True
                bedroom = [lootTable("bedroom"), lootTable("bedroom"), lootTable("bedroom")]
            looting(bedroom)
            return "baseBedroom"
        elif desination == "3":
            print(f"{bcolors.FAIL} FINISH SLEEP LATER {bcolors.ENDC}")
            return "baseBedroom"
        return "baseBedroom"

    def baseBathroom():
        global lootedBaseBathroom
        print(f"{bcolors.OKBLUE}You are in the bathroom.{bcolors.ENDC}")
        print("1. Go back to the hallway")
        print("2. Search the bathroom")
        print("3. Take a shower")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the bathroom.{bcolors.ENDC}")
            return "base"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You find:{bcolors.ENDC}")
            if not lootedBaseBathroom:
                lootedBaseBathroom = True
                bathroom = [lootTable("bathroom"), lootTable("bathroom")]
            looting(bathroom)
            return "baseBathroom"
        elif desination == "3":
            print(f"{bcolors.FAIL} FINISH SHOWERING LATER {bcolors.ENDC}")
            return "baseBathroom"
        return "baseBathroom"

    def park():
        if random.random() < 0.1:
            fightingMiniGame("easy", ZombieGroup("easy"))
        print(f"{bcolors.OKBLUE}You are in the park.{bcolors.ENDC}")
        print("1. Go back to the base")
        print("2. Go to the Suburbs")
        print("3. Go to the playground")
        print("4. Go to the trails")
        print("5. Go to the pavilion")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You go back to the base.{bcolors.ENDC}")
            return "base"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You go to the suburbs.{bcolors.ENDC}")
            return "suburbs"
        elif desination == "3":
            print(f"{bcolors.OKBLUE}You go to the playground.{bcolors.ENDC}")
            return "playground"
        elif desination == "4":
            print(f"{bcolors.OKBLUE}You go to the trails.{bcolors.ENDC}")
            return "trails"
        elif desination == "5":
            print(f"{bcolors.OKBLUE}You go to the pavilion.{bcolors.ENDC}")
            return "pavilion"
        return "park"
        
    def playground():
        global inventory, lootedPlaygroundMonkeyGym, lootedPlaygroundSandbox
        if random.random() < 0.1:
            fightingMiniGame("easy", ZombieGroup("easy"))
        print(f"{bcolors.OKBLUE}You are in the playground.{bcolors.ENDC}")
        print("1. Go back to the park")
        print("2. Go to the monkey gym")
        print("3. Go to the sandbox")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You go back to the park.{bcolors.ENDC}")
            return "park"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You go to the Jungle Gym.{bcolors.ENDC}")
            if not lootedPlaygroundMonkeyGym:
                lootedPlaygroundMonkeyGym = True
                monkeyGym = [lootTable("playgroundMonkeyGym"), lootTable("playgroundMonkeyGym")]
            looting(monkeyGym)
            return "playground"
        elif desination == "3":
            print(f"{bcolors.OKBLUE}You go to the sandbox.{bcolors.ENDC}")
            if not lootedPlaygroundSandbox:
                lootedPlaygroundSandbox = True
                sandbox = [lootTable("playgroundSandbox"), lootTable("playgroundSandbox")]
            looting(sandbox)
            return "playground"
        return "playground"

    def trails():
        global inventory
        if random.random() < 0.1:
            fightingMiniGame("easy", ZombieGroup("easy"))
        print(f"{bcolors.OKBLUE}You are on the trails.{bcolors.ENDC}")
        print("1. Go back to the park")
        print("2. Forage")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You go back to the park.{bcolors.ENDC}")
            return "park"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You find:{bcolors.ENDC}")
            looting([lootTable("trails"), lootTable("trails"), lootTable("trails")])
            return "trails"
        return "trails"

    def pavilion():
        if random.random() < 0.1:
            fightingMiniGame("easy", ZombieGroup("easy"))
        print(f"{bcolors.OKBLUE}You are in the pavilion.{bcolors.ENDC}")
        print("1. Go back to the park")
        print("2. Search the pavilion")
        print("3. Cook something")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You go back to the park.{bcolors.ENDC}")
            return "park"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You find:{bcolors.ENDC}")
            ([lootTable("trails"), lootTable("trails"), lootTable("trails")])
            return "pavilion"
        elif desination == "3":
            print(f"{bcolors.FAIL} FINISH COOKING LATER {bcolors.ENDC}")
            return "pavilion"
        return "pavilion"

    def trailerPark():
        global trailerCOunter
        if random.random() < 0.1:
            fightingMiniGame("easy", ZombieGroup("easy"))
        print(f"{bcolors.OKBLUE}You are in the trailer park.{bcolors.ENDC}")
        print("1. Go back to the base")
        print("2. Go to the suburbs")
        print("3. Search a trailer")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You go back to the base.{bcolors.ENDC}")
            return "base"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You go to the suburbs.{bcolors.ENDC}")
            return "suburbs"
        elif desination == "3":
            print(f"{bcolors.OKBLUE}You search a trailer.{bcolors.ENDC}")
            return "trailerInside"
        return "trailerPark"

    def trailerInside():
        global inventory, leftTrailer, lootedTrailerCabinets, lootedTrailerLoft, lootedTrailerBathroom, leftTrailer
        if random.random() < 0.1:
            fightingMiniGame("easy", ZombieGroup("easy"))
        if lootedTrailerCabinets and lootedTrailerLoft and lootedTrailerBathroom and leftTrailer:
            trailerCounter += 1
            lootedTrailerCabinets = False
            lootedTrailerLoft = False
            lootedTrailerBathroom = False
            leftTrailer = False
        print(f"{bcolors.OKBLUE}You are inside a trailer. You have searched {trailerCounter} trailers.{bcolors.ENDC}")
        print("1. Leave the trailer")
        print("2. Search the cabinets")
        print("3. Search the loft")
        print("4. Search the bathroom")
        if trailerCounter >= 12:
            print(f"{bcolors.OKBLUE}You have looted all the trailers.{bcolors.ENDC}")
            return "trailerPark"
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the trailer.{bcolors.ENDC}")
            if lootedTrailerCabinets and lootedTrailerLoft and lootedTrailerBathroom:
                leftTrailer = True
            return "trailerPark"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You search the cabinets.{bcolors.ENDC}")
            if not lootedTrailerCabinets:
                lootedTrailerCabinets = True
                trailerCabinets = [lootTable("trailerInsideCabinets"), lootTable("trailerInsideCabinets"), lootTable("trailerInsideCabinets")]
            looting(trailerCabinets)
            return "trailerInside"
        elif desination == "3":
            print(f"{bcolors.OKBLUE}You search the loft.{bcolors.ENDC}")
            if not lootedTrailerLoft:
                lootedTrailerLoft = True
                trailerBedroom = [lootTable("bedroom"), lootTable("bedroom"), lootTable("bedroom")]
            looting(trailerBedroom)
            return "trailerInside"
        elif desination == "4":
            print(f"{bcolors.OKBLUE}You search the bathroom.{bcolors.ENDC}")
            if not lootedTrailerBathroom:
                lootedTrailerBathroom = True
                trailerBathroom = [lootTable("bathroom"), lootTable("bathroom"), lootTable("bathroom")]
            looting(trailerBathroom)
            return "trailerInside"
        return "trailerInside"

    def suburbs():
        if random.random() < 0.1:
            fightingMiniGame("medium", ZombieGroup("medium"))
        print(f"{bcolors.OKBLUE}You are in the suburbs.{bcolors.ENDC}")
        print("1. Go to the Trailer Park")
        print("2. Go to the Park")
        print("3. Go to the Hospital")
        print("4. Go to the Apartments")
        print("5. Search a house")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You go to the trailer park.{bcolors.ENDC}")
            return "trailerPark"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You go to the park.{bcolors.ENDC}")
            return "park"
        elif desination == "3":
            print(f"{bcolors.OKBLUE}You go to the hospital.{bcolors.ENDC}")
            return "hospital"
        elif desination == "4":
            print(f"{bcolors.OKBLUE}You go to the apartments.{bcolors.ENDC}")
            return "apartments"
        elif desination == "5":
            print(f"{bcolors.OKBLUE}You search a house.{bcolors.ENDC}")
            return "suburbsInside"
        return "suburbs"

    def suburbsInside():
        global lootedSuburbsKitchen, lootedSuburbsLivingRoom, lootedSuburbsMasterBedroom, lootedSuburbsBedroom, lootedSuburbsBathroom, leftSuburbs, suburbsBedroomCounter, suburbsBathroomCounter
        if(lootedSuburbsKitchen and lootedSuburbsLivingRoom and lootedSuburbsMasterBedroom 
        and lootedSuburbsBedroom and lootedSuburbsBathroom and leftSuburbs):
            suburbsCounter += 1
            lootedSuburbsKitchen = False
            lootedSuburbsLivingRoom = False
            lootedSuburbsMasterBedroom = False
            lootedSuburbsBedroom = False
            lootedSuburbsBathroom = False
            leftSuburbs = False
            suburbsBedroomCounter = random.randint(1, 4)
            suburbsBathroomCounter = random.randint(1, 3)
        if leftSuburbs == False:
            if random.random() < 0.1:
                fightingMiniGame("medium", ZombieGroup("medium"))
        print(f"{bcolors.OKBLUE}You are inside a house. You have searched {suburbsCounter} houses.{bcolors.ENDC}")
        if suburbsCounter >= 10:
            print(f"{bcolors.OKBLUE}You have looted all the houses.{bcolors.ENDC}")
        print("1. Leave the house")
        print("2. Search the Kitchen")
        print("3. Search the Living Room")
        print("4. Search the Bedroom")
        print("5. Search the Bathroom")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the house.{bcolors.ENDC}")
            if lootedSuburbsKitchen and lootedSuburbsLivingRoom and lootedSuburbsBedroom and lootedSuburbsBathroom:
                leftSuburbs = True
            return "suburbs"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You search the kitchen.{bcolors.ENDC}")
            return "suburbsKitchen"
        elif desination == "3":
            print(f"{bcolors.OKBLUE}You search the living room.{bcolors.ENDC}")
            return "suburbsLivingRoom"
        elif desination == "4":
            print(f"{bcolors.OKBLUE}You search a bedroom.{bcolors.ENDC}")
            return "suburbsBedroom"
        elif desination == "5":
            print(f"{bcolors.OKBLUE}You search a bathroom.{bcolors.ENDC}")
            return "suburbsBathroom"
        return "suburbsInside"
        
    def suburbsKitchen():
        global inventory
        if lootedSuburbsKitchen == False:
            if random.random() < 0.1:
                fightingMiniGame("medium", ZombieGroup("medium"))
        print(f"{bcolors.OKBLUE}You are in the Kitchen.{bcolors.ENDC}")
        print("1. Go back to the hallway")
        print("2. Search the kitchen")
        print("3. Cook something")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the kitchen.{bcolors.ENDC}")
            return "suburbsInside"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You find:{bcolors.ENDC}")
            if not lootedSuburbsKitchen:
                lootedSuburbsKitchen = True
                suburbsKitchen = [lootTable("kitchen"), lootTable("kitchen"), lootTable("kitchen")]
            looting(suburbsKitchen)
            return "suburbsKitchen"
        elif desination == "3":
            print(f"{bcolors.FAIL} FINISH COOKING LATER {bcolors.ENDC}")
            return "suburbsKitchen"
        return "suburbsKitchen"

    def suburbsLivingRoom():
        global inventory
        if lootedSuburbsLivingRoom == False:
            if random.random() < 0.1:
                fightingMiniGame("medium", ZombieGroup("medium"))
        print(f"{bcolors.OKBLUE}You are in the living room.{bcolors.ENDC}")
        print("1. Go back to the hallway")
        print("2. Search the living room")
        print("3. Watch TV")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the living room.{bcolors.ENDC}")
            return "suburbsInside"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You find:{bcolors.ENDC}")
            if not lootedSuburbsLivingRoom:
                lootedSuburbsLivingRoom = True
                suburbsLivingRoom = [lootTable("baseLivingRoom"), lootTable("baseLivingRoom")]
            looting(suburbsLivingRoom)
            return "suburbsLivingRoom"
        elif desination == "3":
            print(f"{bcolors.FAIL} FINISH WATCHING TV LATER {bcolors.ENDC}")
            return "suburbsLivingRoom"
        return "suburbsLivingRoom"

    def suburbsBedroom():
        global inventory
        if lootedSuburbsBedroom == False:
            if random.random() < 0.1:
                fightingMiniGame("medium", ZombieGroup("medium"))
        print(f"{bcolors.OKBLUE}You are in the hallway.{bcolors.ENDC}")
        print("1. Go back to the main hallway")
        print("2. Search the master bedroom")
        if suburbsBedroomIndex == False:
            for i in range(suburbsBedroomCounter):
                lootedBedroomCounter.append(0)         
                lootedBedroomCounter.append(0)
                suburbsBedroomIndex = True
        for i in range(suburbsBedroomCounter):
            print(f"{i+3}. Search bedroom {i+1}")
        print(f"{suburbsBedroomCounter+3}. Sleep")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the bedroom hallway.{bcolors.ENDC}")
            return "suburbsInside"
        elif desination == "2":
            print(f"{bcolors.OKBLUE}You search the master bedroom.{bcolors.ENDC}")
            if not lootedSuburbsMasterBedroom:
                lootedSuburbsMasterBedroom = True
                suburbsMasterBedroom = [lootTable("bedroom"), lootTable("bedroom"), lootTable("bedroom")]
            looting(suburbsMasterBedroom)
            return "suburbsBedroom"
        elif desination >= "3":
            index = int(desination) - 3
            if index < suburbsBedroomCounter:
                print(f"{bcolors.OKBLUE}You search bedroom {index+1}.{bcolors.ENDC}")
                if not lootedSuburbsBedroom:
                    if lootedBedroomCounter[index] < 1:
                        suburbsBedroom = [lootTable("bedroom"), lootTable("bedroom"), lootTable("bedroom")]
                increments = looting(suburbsBedroom)
                if increments != 1:
                    lootedBedroomCounter[index] += 1
            elif index == suburbsBedroomCounter:
                print(f"{bcolors.FAIL} FINISH SLEEPING LATER {bcolors.ENDC}")
        return "suburbsBedroom"

    def suburbsBathroom():
        global inventory, suburbsBathroomIndex
        if lootedSuburbsBathroom == False:
            if random.random() < 0.1:
                fightingMiniGame("medium", ZombieGroup("medium"))
        print(f"{bcolors.OKBLUE}You are in the hallway.{bcolors.ENDC}")
        print("1. Go back to the main hallway")
        if suburbsBathroomIndex == False:
            for i in range(suburbsBathroomCounter):
                lootedBathroomCounter.append(0)
            suburbsBathroomIndex = True
        for i in range(suburbsBathroomCounter):
            print(f"{i+2}. Search bathroom {i+1}")
        print(f"{suburbsBathroomCounter+2}. Shower")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print(f"{bcolors.OKBLUE}You leave the bathroom hallway.{bcolors.ENDC}")
            return "suburbsInside"
        elif desination >= "2":
            index = int(desination) - 2
            if index < suburbsBathroomCounter:
                print(f"{bcolors.OKBLUE}You search bathroom {index+1}.{bcolors.ENDC}")
                bathroom = []
                if not lootedSuburbsBathroom:
                    if lootedBathroomCounter[index] < 1:
                        bathroom = [lootTable("bathroom"), lootTable("bathroom"), lootTable("bathroom")]
                if looting(bathroom) != "You take nothing.":
                    lootedBathroomCounter[index] += 1
                    return "suburbsBathroom"
            elif index == suburbsBathroomCounter:
                print(f"{bcolors.FAIL} FINISH SHOWERING LATER {bcolors.ENDC}")
                return "suburbsBathroom"
        return "suburbsBathroom"

    def hospital():
        if random.random() < 0.1:
            fightingMiniGame("medium", ZombieGroup("medium"))
        print("You are in front of the hospital.")
        print("1. Go to the Suburbs")
        print("2. Go to the Police Station")
        print("3. Go inside the Hospital ")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print("You go to the Suburbs")
            return "suburbs"
        elif desination == "2":
            print("You go to the Police Station")
            return "policeStation"
        elif desination == "3":
            print("You go inside the Hospital")
            return "hospitalReception"
        else:
            return "hospital"
        
    def hospitalReception():
        global inventory, lootedHospitalReceptionRooom
        if random.random() < 0.1:
                fightingMiniGame("medium", ZombieGroup("medium"))
        print("You are in the Hospital Reception Office.")
        print("1. Leave the Hospital ")
        print("2. Go to a Medical Room")
        print("3. Go to the Break Room")
        print("4. Search the Reception Office")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print("You leave the hospital.")
            return "hospital"
        if desination == "2":
            print("You enter a Medical Room.")
            return "medicalRoom"
        if desination == "3":
            print("You enter the Break Room.")
            return "breakRoom"
        if desination == "4":
            if lootedHospitalReceptionRooom == False:
                reception = [lootTable("reception"), lootTable("reception"), lootTable("reception")]
                lootedHospitalReceptionRooom = True
            looting(reception)
            return "hospitalReception"
        return "hospitalReception"

    def medicalRoom():
        global inventory
        if random.random() < 0.1:
                fightingMiniGame("medium", ZombieGroup("medium"))
        print("You are in a Medical Room.")
        print("1. Leave the Medical Room")
        print("2. Search the Room")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print("You leave the Medical Room.")
            return "hospital"
        if desination == "2":
            looting([lootTable("medicalRoom"), lootTable("medicalRoom"), lootTable("medicalRoom")])
            return "medicalRoom"
        return "medicalRoom"

    def breakRoom():
        global inventory, lootedHospitalBreakRoom
        if random.random() < 0.1:
                fightingMiniGame("medium", ZombieGroup("medium"))
        print("You are in the Break Room.")
        print("1. Leave the Break Room")
        print("2. Search the Break Room")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print("You leave the Break Room.")
            return "hospitalReception"
        if desination == "2":
            if lootedHospitalBreakRoom == False:
                breakRoom = [lootTable("breakRoom"), lootTable("breakRoom"), lootTable("breakRoom")]
            looting(breakRoom)
            return "breakRoom"
        return "breakRoom"

    def apartments(): 
        if random.random() < 0.1:
                fightingMiniGame("medium", ZombieGroup("medium"))
        print("You are in front of the Apartments.")
        print("1. Go to the Suburbs")
        print("2. Go to the Police Station")
        print("3. Search an Apartment")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print("You go to the Suburbs")
            return "suburbs"
        if desination == "2":
            print("You go to the Police Station.")
            return "policeStation"
        if desination == "3":
            return "apartmentsInside"
        
    def apartmentsInside():
        global inventory
        print("You are inside the Apartment Complex.")
        print("1. Leave the Apartment Complex")
        print("2. Search an Apartment")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print("You leave the Apartment Complex.")
            return "apartments"
        if desination == "2":
            print("You search an Apartment.")
            looting([lootTable("apartment"), lootTable("apartment"), lootTable("apartment")])
            return "apartmentsInside"
        return "apartmentsInside"

    def policeStation():
        print("You are in front of the Police Station.")
        print("1. Go to the Hospital")
        print("2. Go to the Apartments")
        print("3. Go inside the Police Station")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print("You go to the Hospital.")
            return "hospital"
        if desination == "2":
            print("You go to the Apartments.")
            return "apartments"
        if desination == "3":
            print("You go inside the Police Station.")
            return "policeStationInside"

    def policeStationInside():
        print("You are in the Police Station Reception Office")
        print("1. Leave the Police Station")
        print("2. Go to the Locker Room")
        print("3. Go to the Armory")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print("You leave the Police Station.")
            return "policeStation"
        if desination == "2":
            print("You go to the Locker Room.")
            return "policeLockerRoom"
        if desination == "3":
            print("You go to the Armory.")
            return "policeArmory"

    def policeLockerRoom():
        global inventory, lootedPoliceLockerRoom
        print("You are in the Locker Room.")
        print("1. Leave the Locker Room")
        print("2. Search the Locker Room")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print("You leave the Locker Room.")
            return "policeStationInside"
        if desination == "2":
            if lootedPoliceLockerRoom == False:
                lockerRoom = [lootTable("policeLockerRoom"), lootTable("policeLockerRoom"), lootTable("policeLockerRoom")]
                lootedPoliceLockerRoom = True
            looting(lockerRoom)
            return "policeLockerRoom"
        return "policeLockerRoom"

    def policeArmory():
        global inventory
        print("You are in the Armory.")
        print("1. Leave the Armory")
        print("2. Search the Armory")
        desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
        if desination == "1":
            print("You leave the Armory.")
            return "policeStationInside"
        if desination == "2":
            looting([lootTable("policeArmory"), lootTable("policeArmory"), lootTable("policeArmory")])
            return "policeArmory"
        return "policeArmory"

    def debug():
        global inventory
        print("DEBUG ZONE")
        fightingMiniGame("easy", ZombieGroup("easy"))
        #looting([lootTable("policeArmory"), lootTable("policeArmory"), lootTable("policeArmory")])
        return "debug"

#-------------------------------------------------------------------------------#
#                               Main Game Loop                                  #
#-------------------------------------------------------------------------------#
def main():
    global equippedWeapon, equippedArmor, inventory
    location = "base"
    #equippedWeapon = Item("DEBUG WEAPON", 2, 9999, "Slash", 0)
    print(f"{bcolors.OKBLUE}It's the zombie apocalypse, you are low on food. You will need to venture outside soon.{bcolors.ENDC}")    
    while True:
        if health <= 0:
            print("You die")
            break
        command = input(f"{bcolors.WARNING}Enter a command (q to quit, i for inventory, e to equip item, enter to continue):{bcolors.ENDC}").strip()
        if command == "q" or command == "quit":
            break
        if command == "i" or command == "inventory":
            print(f"{bcolors.OKBLUE}Inventory:{bcolors.ENDC}")
            for item in inventory:
                print(f"{item}: {inventory[item].quantity}")
            try: 
                print(f"Equiped Weapon: {equippedWeapon.name}")
            except AttributeError:
                print("No equipped Weapon")
            for item in equippedArmor:
                print(f"Equiped Armor: {item}")
        if command == "e" or command == "equip":
            for i, item in enumerate(inventory):
                print(f"{i+1}. {item}")
            equipItem()
        if command == "" or command == " ":
            pass
        #create location handler and update location
        lochandler = getattr(Location, location)
        location = lochandler()
    print(f"{bcolors.OKBLUE}Final inventory:{bcolors.ENDC}")
    for item in inventory:
        print(f"{item}: {inventory[item].quantity}")
    try:
        print(f"Equiped Weapon: {equippedWeapon}")
    except AttributeError:
        print("No equipped Weapon")
    for item in equippedArmor:
        print(f"Equiped Armor: {item}")
    print(f"{bcolors.OKBLUE}Final Zombie Count {zombieNumber}{bcolors.ENDC}")

if __name__ == "__main__":
    main()
