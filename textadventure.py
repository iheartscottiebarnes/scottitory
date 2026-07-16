import time
inventory = ["torch", "key", "map"]
room = {
    "name": "cave",
    "description": "a dark cave",
    "item": "torch"
}
room2 = {
    "name": "treasureroom",
    "description": "room with two chests",
    "item": "chest1",
    "item2": "chest2"
}
room3 = {
    "name": "furtherdown",
    "description": "room with a locked door"
}
room4 = {
   "name": "winroom",
   "description": "room with hecka gold"
}
haskey = False
hastorch = False
while True:
    try:
        print("You find yourself in a forest. \n"
              "The trail splits into two.")
        forest = input("Do you want to go left or right? (left/right) ")
        if forest.lower() == "left":
            print("You go left.")
            time.sleep(1)
            cave = input("You enter a dark cave and find a torch. \n" \
            "Do you want to go further in or go back? (further/back) ")
            hastorch = True
            if cave.lower() == "further":
                print("You go further in.")
                time.sleep(1)
                door = input("At the end of the cave is a locked door. \n" \
                "Do you want to open it? (yes/no) ")
                if door.lower() == "yes":
                    if haskey == False:
                        print("The door doesn't budge. You go back to the forest.")
                        time.sleep(1.5)
                    elif haskey == True:
                        print("You unlock the door and open it.")
                        time.sleep(1)
                        print("Inside is a room with tons of gold!")
                        time.sleep(1)
                        print("You win!")
                        break
                elif door.lower() == "no":
                    print("You don't open the door, and you go back to the forest.")
                    time.sleep(1)
            elif cave.lower() == "back":
                print("You go back.")
                time.sleep(1)
            else:
                print("pick one bruhhhh")
        elif forest.lower() == "right":
            print("You go right.")
            time.sleep(1)
            if hastorch == True:
             chests = input("You reach find two chests. \n" \
            "Do you want to open the left one or the right one? (left/right) ")
             time.sleep(1)
             if chests.lower() == "left":
              if haskey == False:
                print("You open the left chest...")
                time.sleep(1)
                print("Inside is a key!")
                haskey = True
                time.sleep(1)
                greed = input("Open the other one? ")
                if greed == "yes":
                 print("You open the right chest...")
                 time.sleep(1)
                 print("Inside is a mimic and it swallows you whole.")
                 time.sleep(1)
                 print("Game Over")
                 break
                elif greed == "no":
                 print("You return to the forest.")
                else:
                   print("What?")
              else:
                 print("It's empty. You already took the key.")
                 time.sleep(1)
                 print("You return to the forest.")
                 time.sleep(1)
             elif chests.lower() == "right":
                print("You open the right chest...")
                time.sleep(1)
                print("Inside is a mimic and it swallows you whole.")
                time.sleep(1)
                print("Game Over")
                break
            else:
                print("You go down, but you can't see. You go back to the forest.")
                time.sleep(1)
        else: 
            print("you don't go down a path and just sit there i guess")
            time.sleep(1)
    except ValueError:
        print("hehe")
