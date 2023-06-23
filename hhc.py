import time

print("Welcome to Human Health Calulator!")
time.sleep(3)
print("Enter required inputs as necessary")
time.sleep(3)

print("\n")

print("Be ready for the OXYGEN LEVEL TEST")
time.sleep(3)

print("Keep your finger in the oxymeter device and note the reading")
oxygen = float(input("Enter your oxygen level: "))

if oxygen >= 95 and oxygen <= 100:
    print("Your oxygen level is balanced 🥳")
elif oxygen >= 90 and oxygen <= 105:
    print("Your oxygen level is average 😐")
else:
    print("RIP 🪦🪦🪦")

print("\n")
print("Be ready for the TEMPRATURE TEST")
time.sleep(3)

print("Keep the thermometer in your mouth and note the reading")
temprature = float(input("Enter your Temprature (in celcius): "))

if temprature >= 36.1 and temprature <= 37.2:
    print("Your body temprature is normal")
elif temprature >= 34 and temprature <= 39:
    print("Consult a doctor ASAP!")
else:
    print("How are you even alive?!?!")

print("\n")
print("Be ready for the HEARTBEAT TEST")
time.sleep(3)

print("Keep your finger in oxymeter and note the reading of your heartbeat per minute")
hbpm = int(input("Enter your heatbeat per minute: "))

if hbpm >= 60 and hbpm <= 100:
    print("Your hearbeat is in range")
elif hbpm >= 25 and hbpm <=165:
    print("Consult a doctor ASAP!!!")
else:
    print("You are a ghost!")

print("\n")

sum = oxygen+hbpm+temprature

if sum >= 190 and sum <= 237:
    print("You are absolutely healthy")
elif sum >= 170 and sum <= 270:
    print("Your health is average!")
else:
    print("Make funeral arrangements ASAP! (and don't forget to call your relatives 😐🪦 )")