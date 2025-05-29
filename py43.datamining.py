# CSE 231 – Fall 2008 – Project #6: Google Stock Data Mining
def get_data_list(file_name):
   
    data_list = []
    with open(file_name, 'r') as file:
        next(file) 
        for line in file:
            fields = line.strip().split(',')
            if len(fields) >= 7:
                data_list.append(fields)
    return data_list

def get_monthly_averages(data_list):
 
    monthly_totals = {}  

    for row in data_list:
        date = row[0]          
        volume = float(row[5])  
        adj_close = float(row[6])

        year, month = date.split('-')[0:2]
        month_key = f"{month}-{year}"

        total_sale = volume * adj_close

        if month_key not in monthly_totals:
            monthly_totals[month_key] = [0.0, 0.0]

        monthly_totals[month_key][0] += total_sale
        monthly_totals[month_key][1] += volume

   
    monthly_averages_list = []
    for month_key, (total_sales, total_volume) in monthly_totals.items():
        avg_price = total_sales / total_volume
        monthly_averages_list.append((month_key, avg_price))

    return monthly_averages_list

def print_info(monthly_averages_list):
    """Prints the top 6 best and worst months into 'monthly_averages.txt'."""
    monthly_averages_list.sort(key=lambda x: x[1], reverse=True)

    with open("monthly_averages.txt", "w") as outfile:
        outfile.write("6 best months for google stock:\n")
        for month, avg in monthly_averages_list[:6]:
            outfile.write(f"{month}, {avg:.2f}\n")

        outfile.write("\n6 worst months for Google stock:\n")
        for month, avg in monthly_averages_list[-6:]:
            outfile.write(f"{month}, {avg:.2f}\n")

def main():
    file_name = "tablemining.csv"  
    data_list = get_data_list(file_name)
    monthly_averages_list = get_monthly_averages(data_list)
    print_info(monthly_averages_list)

if __name__ == "__main__":
    main()
