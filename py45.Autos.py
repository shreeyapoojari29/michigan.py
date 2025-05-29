import matplotlib.pyplot as plt
import math

def get_data(filename):
    engine_sizes = []
    avg_mpgs = []

    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            try:
                engine_size = float(data[7])
                city_mpg = float(data[9])
                highway_mpg = float(data[10])
                avg_mpg = (city_mpg + highway_mpg) / 2
                engine_sizes.append(engine_size)
                avg_mpgs.append(avg_mpg)
            except (ValueError, IndexError):
                continue  # skip incomplete or invalid lines

    return engine_sizes, avg_mpgs

def least_squares(x_list, y_list):
    N = len(x_list)
    sumX = sum(x_list)
    sumY = sum(y_list)
    sumXY = sum(x*y for x, y in zip(x_list, y_list))
    sumX2 = sum(x**2 for x in x_list)

    denominator = N * sumX2 - sumX**2
    if denominator == 0:
        raise ValueError("Cannot compute regression: all x values are the same.")

    slope = (N * sumXY - sumX * sumY) / denominator
    intercept = (sumY - slope * sumX) / N
    return slope, intercept

def correlation(x_list, y_list):
    N = len(x_list)
    sumX = sum(x_list)
    sumY = sum(y_list)
    sumXY = sum(x*y for x, y in zip(x_list, y_list))
    sumX2 = sum(x**2 for x in x_list)
    sumY2 = sum(y**2 for y in y_list)

    numerator = N * sumXY - sumX * sumY
    denominator = math.sqrt((N * sumX2 - sumX**2) * (N * sumY2 - sumY**2))
    return numerator / denominator if denominator != 0 else 0

def plot_data(x, y, slope, intercept):
    plt.scatter(x, y, color='blue', label='Car data')
    regression_line = [slope * xi + intercept for xi in x]
    plt.plot(x, regression_line, color='red', label='Regression Line')
    plt.xlabel("Engine Size (liters)")
    plt.ylabel("Average MPG")
    plt.title("Engine Size vs Average MPG")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    filename = "04cars.txt"
    x_vals, y_vals = get_data(filename)

    print(f"Loaded {len(x_vals)} valid data points.")

    if len(x_vals) < 2:
        print("Not enough valid data to perform regression.")
        return

    if all(x == x_vals[0] for x in x_vals):
        print("All engine sizes are the same. Cannot compute regression.")
        return

    try:
        slope, intercept = least_squares(x_vals, y_vals)
        corr = correlation(x_vals, y_vals)

        print(f"Slope: {slope:.4f}")
        print(f"Intercept: {intercept:.4f}")
        print(f"Correlation Coefficient: {corr:.4f}")

        plot_data(x_vals, y_vals, slope, intercept)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
