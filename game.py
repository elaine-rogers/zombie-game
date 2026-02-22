import random
import locations

visitedBase = lootedBaseKitchen = lootedBaseLivingRoom = lootedBaseBedroom = lootedBaseBathroom = leftTrailer = lootedTrailerCabinets = lootedTrailerLoft = lootedHospitalBreakRoom = lootedPoliceLockerRoom = lootedPoliceArmory = suburbsBathroomIndex = lootedHospitalReceptionRooom = False
lootedTrailerBathroom = lootedPlaygroundMonkeyGym = lootedPlaygroundSandbox = leftSuburbs = lootedSuburbsKitchen = lootedSuburbsLivingRoom = lootedSuburbsMasterBedroom = lootedSuburbsBedroom = lootedSuburbsBathroom = suburbsBathroomIndex = False
kitchen, livingRoom, bedroom, bathroom, trailerCabinets, trailerBedroom, trailerBathroom, monkeyGym, sandbox, suburbsKitchen, suburbsLivingRoom, suburbsMasterBedroom, suburbsBedroom, lootedBedroomCounter,lootedBathroomCounter, lockerRoom= ([] for i in range(16))
trailerCounter = suburbsCounter = 0
suburbsBedroomCounter = random.randint(1, 4)
suburbsBathroomCounter = random.randint(1, 3)
inventory = {}

class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def main():
    location = "trailerInside"
    print(f"{bcolors.OKBLUE}It's the zombie apocalypse, you are low on food. You will need to venture outside soon.{bcolors.ENDC}")
    
    while True:
        command = input(f"{bcolors.WARNING}Enter a command (q to quit, i for inventory, enter to continue):{bcolors.ENDC}").strip()
        if command == "q" or command == "quit":
            break
        if command == "i" or command == "inventory":
            print(f"{bcolors.OKBLUE}Inventory:{bcolors.ENDC}")
            for item in inventory:
                print(f"{item}: {inventory[item]['quantity']}")
        if command == "" or command == " ":
            pass
        #create location handler and update location
        lochandler = getattr(locations, location)
        location = lochandler(inventory)
    print(f"{bcolors.OKBLUE}Final inventory: {inventory}{bcolors.ENDC}")

if __name__ == "__main__":
    main()
