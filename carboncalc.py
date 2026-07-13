
input1= input("how many hours per day are you on your computer? ")
input2= input("how many showers does your household take per day? ")
input3= input("how many lights are in your household?  ")
input4= input("how many hours per day are your lights on? ")
input5= input("how many meals are cooked per day? ")
input6= input("what kind of stove do you use? (induction, gas, electric) ")
input7= input("what do you take a trip by? (electric car, gas car, hybrid car, light rail,  bus, plane, ferry)")
input8= input(f"how many trips on {input7} do you take?")
computer_carbon = float(input1) * 60
shower_carbon = float(input2) * 1.2
lights_carbon = float(input3) * float(input4) * 0.045
stove_emissions = {"induction": 0.18, "gas": 0.45, "electric": 0.30}
trip_emissions = {
    "electric car": 0.2,
    "gas car": 0.4,
    "hybrid car": 0.25,
    "light rail": 0.1,
    "bus": 0.15,
    "plane": 0.8,
    "ferry": 0.12
}
meals_carbon = float(input5) * stove_emissions.get(input6.lower(), 0)
trip_carbon = float(input8) * trip_emissions.get(input7.lower(), 0)
print("your shower carbon footprint is: " + str(shower_carbon) + " kg of CO2 per day")
print("your computer carbon footprint is: " + str(computer_carbon) + "g of CO2 per day")
print("your lights carbon footprint is: " + str(lights_carbon) + "lbs of CO2 per day")
if input6 == "induction":
    print("your meals carbon footprint is: " + str(meals_carbon) + "kg of CO2 per day")
if input6 == "gas":
    print("your meals carbon footprint is: " + str(meals_carbon) + "kg of CO2 per day")
if input6 == "electric":
    print("your meals carbon footprint is: " + str(meals_carbon) + "kg of CO2 per day")
if input7 == "electric car":
    print("your trip carbon footprint is: " + str(trip_carbon["electric car"]) + "g of CO2 per day")
if input7 == "gas car":
    print("your trip carbon footprint is: " + str(trip_carbon["gas car"]) + "kg of CO2 per day")
if input7 == "hybrid car":
    print("your trip carbon footprint is: " + str(trip_carbon["hybrid car"]) + "g of CO2 per day")
    if input7 == "light rail":
        print("your trip carbon footprint is: " + str(trip_carbon["light rail"]) + "lbs of CO2 per day")
        if input7 == "bus":
            print("your trip carbon footprint is: " + str(trip_carbon["bus"]) + "lbs of CO2 per day")
            if input7 == "plane":
                print("your trip carbon footprint is: " + str(trip_carbon["plane"]) + "tons of CO2 per day")
                if input7 == "ferry":
                    print("your trip carbon footprint is: " + str(trip_carbon["ferry"]) + "oz of CO2 per day")