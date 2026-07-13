import time
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
       break

if pet_type == 1:
            pet = "dog"
elif pet_type == 2:
            pet = "cat"
else:
            pet = "dragon"
    

print("You have selected a", pet + "! It will hatch in 10 seconds.")
hatch = 10
while hatch > 0:
       hatch -= 1
       time.sleep(1)
print(pet_name, "the", pet, "has hatched!"\f
      "Their stats are..."\f
      "Hunger =", hunger)
    

       

hunger = 80
happiness = 100
energy = 100
health = 100
cleanliness = 100


