# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
total_month = 0
net_total = 0
row_counter = 0
monthly_change = 0
previous_mon=0
current_mon = 0
Monthly_change_list = []
greatest_increase_mon = ""
greatest_decrease_mon = ""
greatest_increase = 0
greatest_decrease = 0
#  Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        row_counter += 1
        # print(str(row_counter) + ":" + row[0] + ", " + row[1])
        total_month += 1
        net_total += int(row[1])
        if (row_counter == 1): 
            previous_mon = int(row[1])
        else:
            current_mon = int(row[1])
            monthly_change = current_mon - previous_mon
            Monthly_change_list.append(monthly_change)
            previous_mon = int(row[1])
            
            if (monthly_change > 0) and (greatest_increase < monthly_change): 
                greatest_increase = monthly_change
                greatest_increase_mon = row[0]
            elif (monthly_change < 0) and (greatest_decrease > monthly_change):
                greatest_decrease = monthly_change
                greatest_decrease_mon = row[0]


    average_monthly_change = sum(Monthly_change_list) / len(Monthly_change_list)
    print('Financial Analysis')
    print("----------------------------")
    print("Total Months: " + str(total_month))
    print("Total: $" + str(net_total))
    print("Average Change: $" + str(round(average_monthly_change,2)))
    print("Greatest Increase in Profits: " + str(greatest_increase_mon) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(greatest_decrease_mon) +  " ($" + str(greatest_decrease) + ")")

    
    # Store the file path associated with the file (note the backslash may be OS specific)
    file = open('analysis/pybank.txt', "w")
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: " + str(total_month) + "\n")
    file.write("Total: $" + str(net_total) + "\n")
    file.write("Average Change: $" + str(round(average_monthly_change,2)) + "\n")
    file.write("Greatest Increase in Profits: " + str(greatest_increase_mon) + " ($" + str(greatest_increase) + ")\n")
    file.write("Greatest Decrease in Profits: " + str(greatest_decrease_mon) +  " ($" + str(greatest_decrease) + ")\n")
    file.close()


   