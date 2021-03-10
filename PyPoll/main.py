
import csv
import collections as collect
#define total votes
total_votes = 0
vote_percent = float
pypoll_csv = "Resources/election_data.csv"
with open(pypoll_csv) as csvfile:

    votes = collect.Counter()
    reader = csv.reader(csvfile)
    header  = next(reader)
    for line in reader:
        candidate = line[-1]
        votes[candidate] += 1
        total_votes += 1

print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for name in votes:
    percent_total = votes[name]/total_votes
    percentages = "{:.3%}".format(percent_total)
    print(f"{name}: {percentages}  ({votes[name]})")



 # Store the file path associated with the file (note the backslash may be OS specific)
    file = open('analysis/pypoll.txt', "w")
    file.write("Election Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Votes: " + str(total_month) + "\n")
    file.write("----------------------------\n")
    file.write(f"{name}: {votes[name]}" "\n")
    file.write("Average Change: $" + str(round(average_monthly_change,2)) + "\n")
    file.write("Greatest Increase in Profits: " + str(greatest_increase_mon) + " ($" + str(greatest_increase) + ")\n")
    file.write("Greatest Decrease in Profits: " + str(greatest_decrease_mon) +  " ($" + str(greatest_decrease) + ")\n")
    file.close()

