
import pathlib
import csv

csvpath = pathlib.Path('./Resources/budget_data.csv')


total_months = 0
total_amount = 0
average_changes = 0
changes = 0
current_amount = 0
pervious_amount = 0
profits = ['profits', 0]
losses = ['losses', 0]


with open(csvpath) as csvfile:
    csvdata = csv.reader(csvfile, delimiter=',')

    # print(csvdata)

    csv_header = next(csvdata)
    # print(f"CSV Header {csv_header}")
    
    for row in csvdata:
        current_amount = int(row[1])
        total_months += 1
        total_amount += current_amount

        if(total_months > 1):
            changes = current_amount - pervious_amount
        # print(f"1: {changes}")

        average_changes += changes
        # print(f"2: {average_changes}")

        pervious_amount = current_amount
        
        if(current_amount > int(profits[1])):
            profits = row
        if(current_amount < int(losses[1])):
            losses = row

        # user = input("next")

txtpath = pathlib.Path('./analysis/result.txt')

with open(txtpath, 'w') as textfile:
    # Print result
    # print(f"2: {average_changes}"
    
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_amount}\n")
    textfile.write(f"Average Change: ${round(average_changes/(total_months-1),2)}\n")
    textfile.write(f"Greatest Increase in Profits: {profits[0]} (${profits[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {losses[0]} (${losses[1]})\n")

