import math

number = int(input("How many manufactured items? "))
items_per_box = int(input("How many items will be packed per box? "))

box = number / items_per_box

print(math.ceil(box))