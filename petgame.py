import time
bar = "-"*10

hunger = 80
happiness = 100
energy = 100
health = 100

hungerbar = "X"*(hunger // 10)
happinessbar = "X"*(happiness // 10)
energybar = "X"*(energy // 10)
healthbar = "X"*(health // 10)


print(bar + "Welcome to the Digital Pet Game!" + bar)

pet_name = input("What is your pet's name?:")

while True: 
    try:
        pet_type = int(input("What kind of pet do you want? 1 = dog, 2 = cat, 3 = dragon:"))
        if 1<= pet_type <4:
            break
        else: 
            print("Number must be 1, 2, or 3")
    except ValueError:
       print("Must be an integer")

if pet_type == 1:
            pet = "dog 🐕"
elif pet_type == 2:
            pet = "cat 🐈"
else:
            pet = "dragon 🐉"
    

print("You have selected a", pet + "! It will hatch in 10 seconds.")
hatch = 10
while hatch > 0:
       hatch -= 1
       time.sleep(0)
       print(hatch, "seconds remaining")
print(f"Your {pet} has hatched! Its stats are: \n"
      f"Hunger: [{hungerbar}] \n"
      f"Happiness: [{happinessbar}] \n"
      f"Energy: [{energybar}] \n"
      f"Health: [{healthbar}] \n"
      f"Make sure to keep {pet_name}'s health above 0, or else.")
turn = 1
while turn < 6:
    try:
         print("turn", turn)
         turn += 1
         hunger = hunger - 10
         happiness = happiness - 5
         if pet_type == 3:
               hunger = hunger - 10
         if hunger == 0:
               health = health - 15
               print("starvation penalty")
         if hunger > 100:    
             hunger = 100
         if happiness > 100:
             happiness = 100
         if energy > 100:
             energy = 100
         if hunger < 0:
               hunger = 0
         if happiness < 0:
               happiness = 0
         if energy < 0:
               energy = 0
         activity=int(input("What do you want to do? 1 = Feed, 2 = Play, 3 = Sleep, 4 = View Stats: "))
         if activity == (1, 2, 3):
               hunger = hunger - 10
               happiness = happiness - 5  
         if activity == 1:
                if hunger < 100:
                    hunger = hunger + 25
                    happiness = happiness + 10
                    health = health - 5
                    print(f"you feed {pet_name}! hunger plus 25, happiness plus ten, health minus 5")
                else:
                    print("this stat max twin don't overfeed lil bro")
         if activity == 2:
                if happiness == 100:
                    print(f"this stat max twin but your {pet} is ecstatic")
                elif 79 < happiness <= 99:
                 happiness = happiness + 25
                 hunger = hunger - 15
                 health = health + 5
                 print(f"you play with your pet. happiness plus 25, hunger minus 15, health plus 5. your {pet} is ecstatic")
                elif 59 < happiness <= 79:
                 happiness = happiness + 25
                 hunger = hunger - 15
                 health += 5
                 print(f"you play with your pet. happiness plus 25, hunger minus 15, health plus 5. your {pet} is happy")
                elif 39 < happiness <= 59:
                 happiness += 25
                 hunger -= 15
                 health += 5
                 print(f"you play with your pet. happiness plus 25, hunger minus 15, health plus 5. your {pet} is okay")
                elif 19 < happiness <= 39:
                 happiness += 25
                 hunger -= 15
                 health += 5
                 print(f"you play with your pet. happiness plus 25, hunger minus 15, health plus 5. your {pet} is sad")
                elif 0 <= happiness <= 19:
                 happiness += 25
                 hunger -= 15
                 health += 5
                 print(f"you play with your pet. happiness plus 25, hunger minus 15, health plus 5. your {pet} is MISERABLE")
         if activity == 3:
             if energy == 100:
                  print(f"bro {pet_name} is fully rested")
             else:
                  print("your pet sleeps. health plus 20, happiness plus 10, hunger minus 10")
                  health += 20
                  happiness += 10
                  hunger -= 10
         if activity == 4:
             print(f"Hunger: [{hungerbar}] \n"
             f"Happiness: [{happinessbar}] \n"
             f"Energy: [{energybar}] \n"
             f"Health: [{healthbar}]")
         if health == 0:
                while True:
                    print("YOU KILLED YOUR PET")   
         if turn == 6:
            print("game over")
            average =(hunger + happiness + health) // 3
            score = average * turn
            if score >= 400:
                  print("legendary")
            elif score >= 300 > 400:
                  print("great")
            elif score >= 200 > 300:
                  print("good")
            else:
                  print("ggs")
    except ValueError:
                print("you bum")

      

      





       

       



