# import math

# def main():
#     with open("can.txt") as can_size:
#         for line in can_size:
#             line = line.strip()  # Move this line before splitting
#             parts = line.split(",")

#             name = parts[0]
#             radius = float(parts[1])
#             height = float(parts[2])
#             amount = float(parts[3])

#             volume = compute_volume(radius, height)
#             surf_area = compute_surface_area(radius, height)
#             efficiency_storage = compute_storage_efficiency(volume, surf_area)
#             print(f"{name} {efficiency_storage:.2f}")

# def compute_volume(radius, height):
#     volume = math.pi * (radius ** 2) * height
#     return volume

# def compute_surface_area(radius, height):
#     surf_area = 2 * math.pi * radius * (radius + height)
#     return surf_area

# def compute_storage_efficiency(volume, area):
#     efficiency = volume / area
#     return efficiency

# main()

# def func1():
#   a=1
# def func2():
#   a=2
#   func1()
#   return a
# a=0
# print(func2())

def fullname(w1,w2):
  return w1 + ' ' + w2

f=fullname(w2='faith',w1='charity')
print(f)
