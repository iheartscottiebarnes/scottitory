import time
step_amount=int(input ("How many steps do you want?:"))

place_steps=(step_amount)
num=step_amount
def place_steps():
    for step in range(step_amount):
     print("place step")
     time.sleep(.25)
    print("Stair complete")
place_steps()

torch_amount=int(input("How many torches do you want to place?"))
torch_places=torch_amount
def place_torches():
   x=1
   for step in range(torch_amount):
    time.sleep(0.25)
    print("placing torch at position (0, ", str(x) + ")")
    x+=1
    if step %5 == 4:
      print("bright torch")
    else:
      print("torch placed") 
place_torches()   

time.sleep(3)

def build_reinforced_wall():
    for wall in range(20):
        time.sleep(0.25)
        if wall %4 == 0:
         print("cobblestone")
        elif wall %5 == 0:
           print("defense reached")
        else:
           print("plank")
    print("wall built successfully")
build_reinforced_wall()

time.sleep(3)

log=0
def collect_logs():
    global log
    while log < 64:
        time.sleep(.25)
        log += 1
        print("Chopping logs...")
    if log >= 60:
        print("Log capacity near full")
        print("Chopping logs...")
    while log == 64:
        print("Max log capacity reached")
        break
collect_logs()

time.sleep(3)

def build_guard_tower(floors, blocks):
    for i in range (floors):
        print("building floor", i + 1)
        time.sleep(1)
        for block in range(blocks):
            time.sleep(.25)
            print("placing block number", block + 1, "in floor", i + 1)
build_guard_tower(5, 5)

time.sleep(3)

energy = 100
print(energy)
def night_patrol():
    global energy
    while energy > 0:
        time.sleep(.25)
        print("patrolling")
        energy -= 12
        print(energy)
        if 0 < energy < 30:
            print("warning low power")
        if energy <= 11:
            energy -= energy
    print(energy)
    print("shutdown")    
night_patrol()


