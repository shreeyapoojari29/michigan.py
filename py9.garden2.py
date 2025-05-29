# Garden Semicircles and Circle Project

import math

def main():
    print("Calculate Garden requirements")
    print("-----------------------------")

    side_length = float(input("Enter length of side of garden (feet): "))
    spacing = float(input("Enter spacing between plants (feet): "))
    bed_depth = float(input("Enter depth of garden soil (feet): "))
    fill_depth = float(input("Enter depth of fill (feet): "))

    print("\n-----------------------------")
    print("Requirements\n")

    radius = side_length / 4

    semicircle_area = (math.pi * radius ** 2) / 2
    circle_area = math.pi * radius ** 2

    total_flowerbed_area = 4 * semicircle_area + circle_area

    garden_area = side_length ** 2

    fill_area = garden_area - total_flowerbed_area

    plant_area = spacing ** 2
    plants_per_semicircle = int(semicircle_area / plant_area)
    plants_center_circle = int(circle_area / plant_area)
    total_plants = 4 * plants_per_semicircle + plants_center_circle

    soil_volume_semicircle = semicircle_area * bed_depth
    soil_volume_circle = circle_area * bed_depth
    total_soil_volume = 4 * soil_volume_semicircle + soil_volume_circle

    soil_volume_semicircle_yds = soil_volume_semicircle / 27
    soil_volume_circle_yds = soil_volume_circle / 27
    total_soil_volume_yds = total_soil_volume / 27

    fill_volume = fill_area * fill_depth
    fill_volume_yds = fill_volume / 27

    print(f"Plants for each semicircle garden: {plants_per_semicircle}")
    print(f"Plants for the circle garden: {plants_center_circle}")
    print(f"Total plants for garden: {total_plants}")

    print(f"Soil for each semicircle garden: {soil_volume_semicircle_yds:.1f} cubic yards")
    print(f"Soil for the circle garden: {soil_volume_circle_yds:.1f} cubic yards")
    print(f"Total soil for the garden: {total_soil_volume_yds:.1f} cubic yards")

    print(f"Total fill for the garden: {fill_volume_yds:.1f} cubic yards")

if __name__ == "__main__":
    main()