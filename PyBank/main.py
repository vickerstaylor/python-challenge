import os
import csv

pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

total = 0
total_months = 1
avg_change_array = []
increase_in_profits = ["", 0]
decrease_in_profits = ["", 500000000]

with open(pybank_csv, newline='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader)
   first_row = next(csvreader)
   previous = int(first_row[1])
   total += int(first_row[1])

   for row in csvreader:
       total_months = total_months + 1
       total = total + int(row[1])
       avg_change = int(row[1]) - previous
       avg_change_array += [avg_change]
       previous = int(row[1])

       if avg_change > increase_in_profits[1]:
           increase_in_profits[0] = row[0]
           increase_in_profits[1] = avg_change

       if avg_change < decrease_in_profits[1]:
           decrease_in_profits[0] = row[0]
           decrease_in_profits[1] = avg_change

total_monthly_avg = sum(avg_change_array) / len(avg_change_array)

var1, var2 = increase_in_profits
var3, var4 = decrease_in_profits

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${total}")
print(f"Average Change: ${round(total_monthly_avg, 2)}")
print(f"Greatest Increase in Profits: {var1} (${var2})")
print(f"Greatest Decrease in Profits: {var3} (${var4})")

with open("pybank.txt", "w", newline='') as f:
    f.write(f"Financial Analysis\n")
    f.write(f"----------------------------\n")
    f.write(f"Total Months: {str(total_months)}\n")
    f.write(f"Total: ${total}\n")
    f.write(f"Average Change: ${round(total_monthly_avg,2)}\n")
    f.write(f"Greatest Increase in Profits: {var1} (${var2})\n")
    f.write(f"Greatest Decrease in Profits: {var3} (${var4})")