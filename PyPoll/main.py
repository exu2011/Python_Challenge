
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
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("----------------------------\n")
    for name in votes:
        percent_total = votes[name]/total_votes
        percentages = "{:.3%}".format(percent_total)
        file.write(name + ": " + str(percentages) + "("  + str(votes[name]) + ")\n")
        
    file.close()

