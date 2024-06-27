import math
from datetime import datetime

pi = math.pi
w = float(input("What is the width in millimeters? "))
a = float (input("What is the aspect ratio of the tire? "))
d = float(input("What is the diameter of the wheel in inches? "))

v = pi * w**2 * a * (w * a + 2540 * d) / 10000000000

print(f"The approximate volume is {v:.2f} liters.")
print()

date = datetime.now()

buy = input("Do you want to purchase the tire with the dimensions you have specified? ")

if buy.lower() == "yes":
    phone = int(input("Please add your phone number: "))
    print("Thank You")
    with open("volumes.txt", mode="at") as volumes_file:
        print(f"{date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {phone}", file=volumes_file)

elif buy.lower() == "no":
    print("Thank You")
    with open("volumes.txt", mode="at") as volumes_file:
        print(f"{date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}", file=volumes_file)





