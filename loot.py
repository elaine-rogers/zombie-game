import random

#loot for class Food. 1 means food
def lootFood():
    if random.random() < 0.5:
        return {"name":"Canned Food", "type": 1, "quantity": 0}
    if random.random() < 0.8:
        return {"name":"Bread", "type": 1, "quantity": 0}
    if random.random() < 0.9:
        return {"name":"Meat", "type": 1, "quantity": 0}
    return {"name":"Cake", "type": 1, "quantity": 0}
        
    #loot for class Kitchen Utensi. 2 means weapons
def lootKitchenUtensil():
    if random.random() < 0.9:
        return {"name":"Rolling Pin", "type": 2, "quantity": 0}
    if random.random() < 0.8:
        return {"name":"Pan", "type": 2, "quantity": 0}
    if random.random() < 0.5:
        return {"name":"Knife", "type": 2, "quantity": 0}
    return {"name":"Pipe Wrench", "type": 2, "quantity": 0}
    
    #loot for class Electronics. 3 means electronics
def lootElectronics():
    if random.random() < 0.8:
        return {"name":"Radio", "type": 3, "quantity": 0}
    if random.random() < 0.5:
        return {"name":"Laptop", "type": 3, "quantity": 0}
    return {"name":"Phone", "type": 3, "quantity": 0} 

#loot for class sheets. 4 means sheets
def lootSheets():
    if random.random() < 0.7:
        return {"name":"Pillow", "type": 4, "quantity": 0}
    return {"name":"Blanket", "type": 4, "quantity": 0}

#loot for class cleaning supplies. 5 means cleaning supplies
def lootCleaningSupplies():
    if random.random() < 0.8:
        return {"name":"Soap", "type": 5, "quantity": 0}
    if random.random() < 0.5:
        return {"name":"Cleaning Spray", "type": 5, "quantity": 0}
    return {"name":"Bleach", "type": 5, "quantity": 0}

#loot for class medical supplies. 6 means medical supplies
def lootMedicalSupplies():
    if random.random() < 0.8:
        return {"name":"Bandages", "type": 6, "quantity": 0}
    if random.random() < 0.5:
        return {"name":"Painkillers", "type": 6, "quantity": 0}
    return {"name":"Antibiotics", "type": 6, "quantity": 0}

#loot for class weapons. 2 means weapons
def lootWeapons():
    if random.random() < 0.8:
        return {"name":"Baseball Bat", "type": 2, "quantity": 0}
    if random.random() < 0.5:
        return {"name":"Crowbar", "type": 2, "quantity": 0}
    return {"name":"Machete", "type": 2, "quantity": 0}

#loot for class shovels. Offshoot of weapons
def lootShovels():
    if random.random() < 0.8:
        return {"name":"Spade", "type": 2, "quantity": 0}
    if random.random() < 0.5:
        return {"name":"Garden Shovel", "type": 2, "quantity": 0}
    return {"name":"Snow Shovel", "type": 2, "quantity": 0}

#loot for toys. 8 means toys
def lootToys():
    if random.random() < 0.8:
        return {"name":"Doll", "type": 7, "quantity": 0}
    if random.random() < 0.5:
        return {"name":"Toy Car", "type": 7, "quantity": 0}
    if random.random() < 0.3:
        return {"name":"Rubik's Cube", "type": 7, "quantity": 0}
    return {"name":"Baseball Bat", "type": 2, "quantity": 0}

#loot for backpacks. 9 means backpacks
def lootBackpacks():
    if random.random() < 0.8:
        return {"name":"School Backpack", "type": 8, "quantity": 0}
    if random.random() < 0.5:
        return {"name":"Hiking Backpack", "type": 8, "quantity": 0}
    return {"name":"Duffel Bag", "type": 8, "quantity": 0}

#loot for stationary. 10 means stationary
def lootStationary():
    if random.random() < 0.5:
        return {"name":"Notebook", "type": 9, "quantity": 0}
    if random.random() < 0.3:
        return {"name":"Pensil", "type": 9, "quantity": 0}
    if random.random() < 0.3:
        return {"name":"Black Pen", "type": 9, "quantity": 0}
    if random.random() < 0.3:
        return {"name":"Blue Pen", "type": 9, "quantity": 0}
    return {"name":"Red Pen", "type": 9, "quantity": 0}

#loot for funs. Subsection of weapons
def lootGuns():
    if random.random() < 0.7:
        return {"name": "Pistol", "type": 2, "quantity": 0}
    if random.random() < 0.5:
        return {"name": "Rifle", "type": 2, "quantity": 0}
    return {"name": "Shotgun", "type": 2, "quantity": 0}

def lootArmor():
    if random.random() < 0.3:
        return {"name": "Shin and Knee Gaurds", "type": 10, "quantity": 0}
    if random.random() < 0.3:
        return {"name": "Arm Gaurds", "type": 10, "quantity": 0}
    if random.random() < 0.3:
        return {"name": "Bullet Proof Vest", "type": 10, "quantity": 0}
    if random.random() < 0.3:
        return {"name": "Riot Helmet", "type": 10, "quantity": 0}
    return {"name": "Riot Shield", "type": 10, "quantity": 0}       
            
#Loot table for different areas
def lootTable(area):
    if area == "kitchen":
        if random.random() < 0.1:
            return lootKitchenUtensil()
        return lootFood()
    elif area == "baseLivingRoom":
        return lootElectronics()
    elif area == "bedroom":
        if(random.random() < 0.1):
            return lootElectronics()
        return lootSheets()
    elif area == "bathroom":
        if random.random() < 0.7:
            return lootCleaningSupplies()
        return lootMedicalSupplies()
    elif area == "trailerInsideCabinets":
        if random.random() < 0.7:
            return lootFood()
        if random.random() < 0.5:
            return lootKitchenUtensil()
        if random.random() < 0.3:
            return lootCleaningSupplies()
        if random.random() < 0.1:
            return lootMedicalSupplies()
        if random.random() < 0.1:
            return lootKitchenUtensil()
        return lootWeapons()
    elif area == "playgroundMonkeyGym":
        if random.random() < 0.9:
            return lootToys()
        return lootBackpacks()
    elif area == "playgroundSandbox":
        if random.random() < 0.9:
            return lootToys()
        if random.random() < 0.5:
            return lootShovels()
        return lootBackpacks()
    elif area == "trails":
        if random.random() < 0.05:
            return lootFood()
        if random.random() < 0.05:
            return lootKitchenUtensil()
        if random.random() < 0.05:
            return lootElectronics()
        if random.random() < 0.05:
            return lootSheets()
        if random.random() < 0.05:
            return lootCleaningSupplies()
        if random.random() < 0.05:
            return lootMedicalSupplies()
        if random.random() < 0.05:
            return lootWeapons()
        if random.random() < 0.05:
            return lootToys()
        if random.random() < 0.05:
            return lootBackpacks()
        if random.random() < 0.05:
            return lootStationary()
        return None
    elif area == "reception":
        if random.random() < 0.9:
            return lootStationary()
        return lootElectronics()
    elif area == "medicalRoom":
        return lootMedicalSupplies()
    elif area == "breakRoom":
        if random.random() < 0.5:
            return lootFood()
        if random.random() < 0.3:
            return lootElectronics()
        return lootStationary()
    elif area == "apartment":
        if random.random() < 0.05:
            return lootFood()
        if random.random() < 0.05:
            return lootKitchenUtensil()
        if random.random() < 0.05:
            return lootElectronics()
        if random.random() < 0.05:
            return lootSheets()
        if random.random() < 0.05:
            return lootCleaningSupplies()
        if random.random() < 0.05:
            return lootMedicalSupplies()
        if random.random() < 0.05:
            return lootWeapons()
        if random.random() < 0.05:
            return lootToys()
        if random.random() < 0.05:
            return lootShovels()
        if random.random() < 0.05:
            return lootBackpacks()
        if random.random() < 0.05:
            return lootStationary()
    elif area == "policeLockerRoom":
        if random.random() < 0.5:
            return lootFood()
        if random.random() < 0.5:
            return lootGuns()
        return lootArmor()
    elif area == "policeArmory":
        if random.random() < 0.5:
            return lootGuns()
        return lootArmor()
