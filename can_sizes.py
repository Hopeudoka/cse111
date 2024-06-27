import math

def main():
    with open("can.txt") as can_size:
        for line in can_size:
            line = line.strip()
            parts = line.split(",")

            name = parts[0]
            radius = float(parts[1])
            height = float(parts[2])
            # amount = float(parts[3])

            volume = compute_volume(radius, height)
            surf_area = compute_surface_area(radius, height)
            efficiency_storage = compute_storage_efficiency(volume, surf_area)
            print(f"{name} {efficiency_storage:.2f}")

def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

def compute_surface_area(radius, height):
  # surface = 2 * math.pi * radius * (radius + height)
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area

def compute_storage_efficiency(volume, area):
  efficiency = volume / area
  return efficiency

main()