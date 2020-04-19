
import pathlib
import csv

csvpath = pathlib.Path('./Resources/election_data.csv')
txtpath = pathlib.Path('./analysis/result.txt')

candidate = ["Khan", "Correy", "Li", "O'Tooley"]
candidate_count = [0, 0, 0, 0]
candidate_percentage = [0, 0, 0, 0]

total_votes = 0

with open(csvpath) as csvfile:
    csvdata = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvdata)

    for row in csvdata:
        total_votes += 1 # Increase votes count
        # Loop through the candidate count
        for i in range(4):
            if(row[2] == candidate[i]):
                candidate_count[i] += 1
    # Calculate the percentage
    for i in range(4):
        candidate_percentage[i] = candidate_count[i] / total_votes * 100

with open(txtpath, 'w') as textfile:

    textfile.write("Election Results\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("----------------------------\n")
    for i in range(4):
        textfile.write(f"{candidate[i]}: {round(candidate_percentage[i])}.000% ({candidate_count[i]})\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Winner: {candidate[candidate_count.index(max(candidate_count))]}\n")
    textfile.write("----------------------------\n")