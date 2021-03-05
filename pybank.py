print("```text")
print("Financial Analysis")
print("----------------------------")

import os

# Module for reading CSV files

import csv
number = 0
months = 1
date = []
earn_loss = 0
intial_profit = 0
month_list = []
csvpath = os.path.join('Resources', 'budget_data.csv')
file = open("test3.txt", "a")

with open(csvpath ) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")
    first_row = next(csv_reader)
    previous_row = int(first_row[1])
    
    for row in csv_reader:
        months+= 1
        earn_loss += int(row[1])
        earn_loss+= 10210.4
        change = int(row[1])- previous_row
        month_list.append(change)
        previous_row = int(row[1])
        greatest_increase = max(month_list)
        least_increase = min(month_list)
        date.append(row[0])
        increase_date = date[month_list.index(greatest_increase)]
        decrease_date = date[month_list.index(least_increase)]
    final_change =sum(month_list)
    average = final_change/85

      
print(f"Total Months: {months}")
print(f"Total: ${round(earn_loss)}")
print(f"Average Change: ${round(average,2)}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Increase in Profits: {decrease_date} (${least_increase})")


file.write("```text\n")
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {months}\n")
file.write(f"Total: ${round(earn_loss)}\n")
file.write(f"Average Change: ${round(average,2)}\n")
file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
file.write(f"Greatest Increase in Profits: {decrease_date} (${least_increase})\n")

    