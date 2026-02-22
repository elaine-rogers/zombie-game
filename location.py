import random
import game
import inventory
import loot

class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def base(mainInventory):
    if not game.visitedBase:
        print(f"{bcolors.OKBLUE}You are in a small cabin on the outskirts of town.{bcolors.ENDC}")
        game.visitedBase = True
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
    
def outsideBase(mainInventory):
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

def baseKitchen(mainInventory):
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
        if not game.lootedBaseKitchen:
            game.lootedBaseKitchen = True
            game.kitchen = [loot.lootTable("kitchen"), loot.lootTable("kitchen"), loot.lootTable("kitchen")]
        inventory.looting(mainInventory, game.kitchen, 0)
        return "baseKitchen"
    elif desination == "3":
        print(f"{bcolors.FAIL} FINISH COOKING LATER {bcolors.ENDC}")
        return "baseKitchen"
    return "baseKitchen"
    
def baseLivingRoom(mainInventory):
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
        if not game.lootedBaseLivingRoom:
            game.lootedBaseLivingRoom = True
            game.livingRoom = [loot.lootTable("baseLivingRoom"), loot.lootTable("baseLivingRoom")]
        inventory.looting(mainInventory, game.livingRoom, 0)
        return "baseLivingRoom"
    elif desination == "3":
        print(f"{bcolors.FAIL} FINISH WATCHING TV LATER {bcolors.ENDC}")
        return "baseLivingRoom"
    return "baseLivingRoom"
    
def baseBedroom(mainInventory):
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
        if not game.lootedBaseBedroom:
            game.lootedBaseBedroom = True
            game.bedroom = [loot.lootTable("bedroom"), loot.lootTable("bedroom"), loot.lootTable("bedroom")]
        inventory.looting(mainInventory, game.bedroom, 0)
        return "baseBedroom"
    elif desination == "3":
        print(f"{bcolors.FAIL} FINISH SLEEP LATER {bcolors.ENDC}")
        return "baseBedroom"
    return "baseBedroom"

def baseBathroom(mainInventory):
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
        if not game.lootedBaseBathroom:
            game.lootedBaseBathroom = True
            game.bathroom = [loot.lootTable("bathroom"), loot.lootTable("bathroom")]
        inventory.looting(mainInventory, game.bathroom, 0)
        return "baseBathroom"
    elif desination == "3":
        print(f"{bcolors.FAIL} FINISH SHOWERING LATER {bcolors.ENDC}")
        return "baseBathroom"
    return "baseBathroom"

def park(mainInventory):
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
    
def playground(mainInventory):
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
        if not game.lootedPlaygroundMonkeyGym:
            game.lootedPlaygroundMonkeyGym = True
            game.monkeyGym = [loot.lootTable("playgroundMonkeyGym"), loot.lootTable("playgroundMonkeyGym")]
        inventory.looting(mainInventory, game.monkeyGym, 0)
        return "playground"
    elif desination == "3":
        print(f"{bcolors.OKBLUE}You go to the sandbox.{bcolors.ENDC}")
        if not game.lootedPlaygroundSandbox:
            game.lootedPlaygroundSandbox = True
            game.sandbox = [loot.lootTable("playgroundSandbox"), loot.lootTable("playgroundSandbox")]
        inventory.looting(mainInventory, game.sandbox, 0)
        return "playground"
    return "playground"

def trails(mainInventory):
    print(f"{bcolors.OKBLUE}You are on the trails.{bcolors.ENDC}")
    print("1. Go back to the park")
    print("2. Forage")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        print(f"{bcolors.OKBLUE}You go back to the park.{bcolors.ENDC}")
        return "park"
    elif desination == "2":
        print(f"{bcolors.OKBLUE}You find:{bcolors.ENDC}")
        inventory.looting(mainInventory, [loot.lootTable("trails"), loot.lootTable("trails"), loot.lootTable("trails")], 0)
        return "trails"
    return "trails"

def pavilion(mainInventory):
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
        inventory.looting(mainInventory,[ loot.lootTable("trails"), loot.lootTable("trails"), loot.lootTable("trails")], 0)
        return "pavilion"
    elif desination == "3":
        print(f"{bcolors.FAIL} FINISH COOKING LATER {bcolors.ENDC}")
        return "pavilion"
    return "pavilion"

def trailerPark(mainInventory):
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

def trailerInside(mainInventory):
    if game.lootedTrailerCabinets and game.lootedTrailerLoft and game.lootedTrailerBathroom and game.leftTrailer:
        game.trailerCounter += 1
        game.lootedTrailerCabinets = False
        game.lootedTrailerLoft = False
        game.lootedTrailerBathroom = False
        game.leftTrailer = False
    print(f"{bcolors.OKBLUE}You are inside a trailer. You have searched {game.trailerCounter} trailers.{bcolors.ENDC}")
    print("1. Leave the trailer")
    print("2. Search the cabinets")
    print("3. Search the loft")
    print("4. Search the bathroom")
    if game.trailerCounter >= 12:
        print(f"{bcolors.OKBLUE}You have looted all the trailers.{bcolors.ENDC}")
        return "trailerPark"
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        print(f"{bcolors.OKBLUE}You leave the trailer.{bcolors.ENDC}")
        if game.lootedTrailerCabinets and game.lootedTrailerLoft and game.lootedTrailerBathroom:
            game.leftTrailer = True
        return "trailerPark"
    elif desination == "2":
        print(f"{bcolors.OKBLUE}You search the cabinets.{bcolors.ENDC}")
        if not game.lootedTrailerCabinets:
            game.lootedTrailerCabinets = True
            game.trailerCabinets = [loot.lootTable("trailerInsideCabinets"), loot.lootTable("trailerInsideCabinets"), loot.lootTable("trailerInsideCabinets")]
        inventory.looting(mainInventory, game.trailerCabinets, 0)
        return "trailerInside"
    elif desination == "3":
        print(f"{bcolors.OKBLUE}You search the loft.{bcolors.ENDC}")
        if not game.lootedTrailerLoft:
            game.lootedTrailerLoft = True
            game.trailerBedroom = [loot.lootTable("bedroom"), loot.lootTable("bedroom"), loot.lootTable("bedroom")]
        inventory.looting(mainInventory, game.trailerBedroom, 0)
        return "trailerInside"
    elif desination == "4":
        print(f"{bcolors.OKBLUE}You search the bathroom.{bcolors.ENDC}")
        if not game.lootedTrailerBathroom:
            game.lootedTrailerBathroom = True
            game.trailerBathroom = [loot.lootTable("bathroom"), loot.lootTable("bathroom"), loot.lootTable("bathroom")]
        inventory.looting(mainInventory, game.trailerBathroom, 0)
        return "trailerInside"
    return "trailerInside"

def suburbs(mainInventory):
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

def suburbsInside(mainInventory):
    if(game.lootedSuburbsKitchen and game.lootedSuburbsLivingRoom and game.lootedSuburbsMasterBedroom 
       and game.lootedSuburbsBedroom and game.lootedSuburbsBathroom and game.leftSuburbs):
        game.suburbsCounter += 1
        game.lootedSuburbsKitchen = False
        game.lootedSuburbsLivingRoom = False
        game.lootedSuburbsMasterBedroom = False
        game.lootedSuburbsBedroom = False
        game.lootedSuburbsBathroom = False
        game.leftSuburbs = False
        game.suburbsBedroomCounter = random.randint(1, 4)
        game.suburbsBathroomCounter = random.randint(1, 3)

    print(f"{bcolors.OKBLUE}You are inside a house. You have searched {game.suburbsCounter} houses.{bcolors.ENDC}")
    if game.suburbsCounter >= 10:
        print(f"{bcolors.OKBLUE}You have looted all the houses.{bcolors.ENDC}")
    print("1. Leave the house")
    print("2. Search the Kitchen")
    print("3. Search the Living Room")
    print("4. Search the Bedroom")
    print("5. Search the Bathroom")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        print(f"{bcolors.OKBLUE}You leave the house.{bcolors.ENDC}")
        if game.lootedSuburbsKitchen and game.lootedSuburbsLivingRoom and game.lootedSuburbsBedroom and game.lootedSuburbsBathroom:
            game.leftSuburbs = True
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
    
def suburbsKitchen(mainInventory):
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
        if not game.lootedSuburbsKitchen:
            game.lootedSuburbsKitchen = True
            game.suburbsKitchen = [loot.lootTable("kitchen"), loot.lootTable("kitchen"), loot.lootTable("kitchen")]
        inventory.looting(mainInventory, game.suburbsKitchen, 0)
        return "suburbsKitchen"
    elif desination == "3":
        print(f"{bcolors.FAIL} FINISH COOKING LATER {bcolors.ENDC}")
        return "suburbsKitchen"
    return "suburbsKitchen"

def suburbsLivingRoom(mainInventory):
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
        if not game.lootedSuburbsLivingRoom:
            game.lootedSuburbsLivingRoom = True
            game.suburbsLivingRoom = [loot.lootTable("baseLivingRoom"), loot.lootTable("baseLivingRoom")]
        inventory.looting(mainInventory, game.suburbsLivingRoom, 0)
        return "suburbsLivingRoom"
    elif desination == "3":
        print(f"{bcolors.FAIL} FINISH WATCHING TV LATER {bcolors.ENDC}")
        return "suburbsLivingRoom"
    return "suburbsLivingRoom"

def suburbsBedroom(mainInventory):
    print(f"{bcolors.OKBLUE}You are in the hallway.{bcolors.ENDC}")
    print("1. Go back to the main hallway")
    print("2. Search the master bedroom")
    if game.suburbsBedroomIndex == False:
        for i in range(game.suburbsBedroomCounter):
            game.lootedBedroomCounter.append(0)
        game.suburbsBedroomIndex = True
    for i in range(game.suburbsBedroomCounter):
        print(f"{i+3}. Search bedroom {i+1}")
    print(f"{game.suburbsBedroomCounter+3}. Sleep")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        print(f"{bcolors.OKBLUE}You leave the bedroom hallway.{bcolors.ENDC}")
        return "suburbsInside"
    elif desination == "2":
        print(f"{bcolors.OKBLUE}You search the master bedroom.{bcolors.ENDC}")
        if not game.lootedSuburbsMasterBedroom:
            game.lootedSuburbsMasterBedroom = True
            game.suburbsMasterBedroom = [loot.lootTable("bedroom"), loot.lootTable("bedroom"), loot.lootTable("bedroom")]
        inventory.looting(mainInventory, game.suburbsMasterBedroom, 0)
        return "suburbsBedroom"
    elif desination >= "3":
        index = int(desination) - 3
        if index < game.suburbsBedroomCounter:
            print(f"{bcolors.OKBLUE}You search bedroom {index+1}.{bcolors.ENDC}")
            if not game.lootedSuburbsBedroom:
                if game.lootedBedroomCounter[index] < 1:
                    game.suburbsBedroom = [loot.lootTable("bedroom"), loot.lootTable("bedroom"), loot.lootTable("bedroom")]
            increments = inventory.looting(mainInventory, game.suburbsBedroom, 0)
            if increments != 1:
                game.lootedBedroomCounter[index] += 1
        elif index == game.suburbsBedroomCounter:
            print(f"{bcolors.FAIL} FINISH SLEEPING LATER {bcolors.ENDC}")
    return "suburbsBedroom"

def suburbsBathroom(mainInventory):
    print(f"{bcolors.OKBLUE}You are in the hallway.{bcolors.ENDC}")
    print("1. Go back to the main hallway")
    if game.suburbsBathroomIndex == False:
        for i in range(game.suburbsBathroomCounter):
            game.lootedBathroomCounter.append(0)
        game.suburbsBathroomIndex = True
    for i in range(game.suburbsBathroomCounter):
        print(f"{i+2}. Search bathroom {i+1}")
    print(f"{game.suburbsBathroomCounter+2}. Shower")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        print(f"{bcolors.OKBLUE}You leave the bathroom hallway.{bcolors.ENDC}")
        return "suburbsInside"
    elif desination >= "2":
        index = int(desination) - 2
        if index < game.suburbsBathroomCounter:
            print(f"{bcolors.OKBLUE}You search bathroom {index+1}.{bcolors.ENDC}")
            bathroom = []
            if not game.lootedSuburbsBathroom:
                if game.lootedBathroomCounter[index] < 1:
                    bathroom = [loot.lootTable("bathroom"), loot.lootTable("bathroom"), loot.lootTable("bathroom")]
            if inventory.looting(mainInventory, bathroom, 0) != "You take nothing.":
                game.lootedBathroomCounter[index] += 1
                return "suburbsBathroom"
        elif index == game.suburbsBathroomCounter:
            print(f"{bcolors.FAIL} FINISH SHOWERING LATER {bcolors.ENDC}")
            return "suburbsBathroom"
    return "suburbsBathroom"

def hospital(mainInventory):
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
     
def hospitalReception(mainInventory):
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
        if game.lootedHospitalReceptionRooom == False:
            reception = [loot.lootTable("reception"), loot.lootTable("reception"), loot.lootTable("reception")]
            game.lootedHospitalReceptionRooom = True
        inventory.looting(mainInventory, reception, 0)
        return "hospitalReception"
    return "hospitalReception"

def medicalRoom(mainInventory):
    print("You are in a Medical Room.")
    print("1. Leave the Medical Room")
    print("2. Search the Room")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        print("You leave the Medical Room.")
        return "hospital"
    if desination == "2":
        inventory.looting(mainInventory, [loot.lootTable("medicalRoom"), loot.lootTable("medicalRoom"), loot.lootTable("medicalRoom")], 0)
        return "medicalRoom"
    return "medicalRoom"

def breakRoom(mainInventory):
    print("You are in the Break Room.")
    print("1. Leave the Break Room")
    print("2. Search the Break Room")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        print("You leave the Break Room.")
        return "hospitalReception"
    if desination == "2":
        if game.lootedHospitalBreakRoom == False:
            breakRoom = [loot.lootTable("breakRoom"), loot.lootTable("breakRoom"), loot.lootTable("breakRoom")]
        inventory.looting(mainInventory, breakRoom, 0)
        return "breakRoom"
    return "breakRoom"

def apartments(mainInventory): 
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
    
def apartmentsInside(mainInventory):
    print("You are inside the Apartment Complex.")
    print("1. Leave the Apartment Complex")
    print("2. Search an Apartment")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        print("You leave the Apartment Complex.")
        return "apartments"
    if desination == "2":
        print("You search an Apartment.")
        inventory.looting(mainInventory, [loot.lootTable("apartment"), loot.lootTable("apartment"), loot.lootTable("apartment")], 0)
        return "apartmentsInside"
    return "apartmentsInside"

def policeStation(mainInventory):
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

def policeStationInside(mainInventory):
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

def policeLockerRoom(mainInventory):
    print("You are in the Locker Room.")
    print("1. Leave the Locker Room")
    print("2. Search the Locker Room")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        print("You leave the Locker Room.")
        return "policeStationInside"
    if desination == "2":
        if game.lootedPoliceLockerRoom == False:
            game.lockerRoom = [loot.lootTable("policeLockerRoom"), loot.lootTable("policeLockerRoom"), loot.lootTable("policeLockerRoom")]
            game.lootedPoliceLockerRoom = True
        inventory.looting(mainInventory, game.lockerRoom, 0)
        return "policeLockerRoom"
    return "policeLockerRoom"

def policeArmory(mainInventory):
    print("You are in the Armory.")
    print("1. Leave the Armory")
    print("2. Search the Armory")
    desination = input(f"{bcolors.WARNING}What do you want to do?{bcolors.ENDC}")
    if desination == "1":
        print("You leave the Armory.")
        return "policeStationInside"
    if desination == "2":
        inventory.looting(mainInventory, [loot.lootTable("policeArmory"), loot.lootTable("policeArmory"), loot.lootTable("policeArmory")], 0)
        return "policeArmory"
    return "policeArmory"




     

