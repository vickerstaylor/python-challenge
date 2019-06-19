import os
import csv

pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

# def financial_analysis(budgetdata):
    # months = str(budgetdata[0])
    # pnl = float(budgetdata[1])

with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)
    # for row in csvreader:
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {str(row_count)}")
    print(f"Average Change: ${float()}")
    print(f"Greatest Increase in Profits: {str()} ({float()})")
    print(f"Greatest Decrease in Profits: {str()} ({float()})")