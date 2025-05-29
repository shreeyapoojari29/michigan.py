# Garden Planning Project

import math

def main():
    
    side_length = float(input("Enter the side length of the garden (in feet): "))
    spacing_inches = float(input("Enter the spacing between plants (in inches): "))
    bed_depth = float(input("Enter the depth of the flowerbeds (in feet): "))
    fill_depth = float(input("Enter the depth of the fill areas (in feet): "))

   
    spacing_feet = spacing_inches / 12

    garden_area = side_length * side_length
    triangle_base = side_length / 2
    triangle_area = 0.5 * triangle_base * triangle_base
    total_triangle_area = 4 * triangle_area

    circle_radius = side_length / 4
    circle_area = math.pi * (circle_radius ** 2)

    flowerbeds_area = total_triangle_area + circle_area
    fill_area = garden_area - flowerbeds_area

    plant_area = spacing_feet ** 2
    plants_per_triangle = int(triangle_area / plant_area)
    plants_in_circle = int(circle_area / plant_area)
    total_plants = 4 * plants_per_triangle + plants_in_circle

    soil_volume_triangle = triangle_area * bed_depth
    soil_volume_circle = circle_area * bed_depth
    total_soil_volume = 4 * soil_volume_triangle + soil_volume_circle

    soil_volume_triangle_yards = soil_volume_triangle / 27
    soil_volume_circle_yards = soil_volume_circle / 27
    total_soil_volume_yards = total_soil_volume / 27

    fill_volume = fill_area * fill_depth
    fill_volume_yards = fill_volume / 27


    print("\nGarden Planning Results:")
    print(f"Plants needed per triangular flowerbed: {plants_per_triangle}")
    print(f"Plants needed for circular flowerbed: {plants_in_circle}")
    print(f"Total plants needed: {total_plants}")

    print(f"\nSoil needed per triangular flowerbed: {soil_volume_triangle_yards:.1f} cubic yards")
    print(f"Soil needed for circular flowerbed: {soil_volume_circle_yards:.1f} cubic yards")
    print(f"Total soil needed: {total_soil_volume_yards:.1f} cubic yards")

    print(f"\nTotal fill material needed: {fill_volume_yards:.1f} cubic yards")

if __name__ == "__main__":
    main()
