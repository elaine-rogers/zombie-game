class bcolors:
        OKBLUE = '\033[94m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
#grab something and put it into the inventory    
def putInventory(inventory, item, quant): 
    if item not in inventory:
        inventory[item] = {"quantity": 0}
        prev = inventory[item]["quantity"]
    inventory[item]["quantity"] += quant

#remove something from the inventory
def removeInventory(inventory, item, quant):
    if inventory.get(item, 0) >= quant:
        inventory[item]["quantity"] -= quant
        if inventory[item]["quantity"] <= 0:
            del inventory[item]
        return True
    else:
        return False

#loots the location and adds it to the inventory
def looting(inventory, lootTable, increments):
    lootTable[:] = [loot for loot in lootTable if isinstance(loot, dict)]
    if len(lootTable) == 0:
            print("There is nothing to take")
            return 0
    for loot in lootTable:
        print(loot["name"])
    print("1. Take all")
    print("2. Take specific item")
    print("3. Take nothing")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        for loot in lootTable:
            putInventory(inventory, loot["name"], 1)
        lootTable.clear()
        return 0
    if desination == "2":
        for i in range(len(lootTable)):
            print(f"{i+1}. {lootTable[i]['name']}")
        itemIndex = int(input(f"{bcolors.WARNING}Which item do you want to take?{bcolors.ENDC}")) - 1
        if itemIndex < len(lootTable):
            putInventory(inventory, lootTable[itemIndex]["name"], 1)
            lootTable.pop(itemIndex)
            return 0
    elif desination == "3":
        print(f"{bcolors.OKBLUE}You take nothing.{bcolors.ENDC}")
        return 1
