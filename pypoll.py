print("```text")
print("Election Results")
print("----------------------------")

import os

# Module for reading CSV files

import csv
# "Khan","Correy","Li","O'Tooley"
candidate = []
i_khan = 0
i_Correy = 0
i_Li = 0
i_Tooley = 0
total = 0

# total_voters = 0
# intial_profit = 0
#  vote_list = []

csvpath = os.path.join('Resources', 'election_data.csv')
file = open("test3.txt", "a")
with open(csvpath ) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")
    
    for row in csv_reader:
        total+=1
        # candidate.append(change)
        if row[2] == "Khan":
            i_khan+=1
        if row[2] == "Correy":
             i_Correy+=1
        if row[2] == "Li":
             i_Li+=1
        if row[2] == "O'Tooley":
             i_Tooley+=1
        final_change =(total)
        Khan_percent = (i_khan/final_change)* 100
        Correy_percent = (i_Correy/final_change)* 100
        Li_percent = (i_Li/final_change)* 100
        Tooley_percent = (i_Tooley/final_change)* 100
        max_voters = {"Khan":Khan_percent,'Correy':Correy_percent,'Li':Li_percent,'Tooley':Tooley_percent}
        maxy_voters = (max(i_khan,i_Correy,i_Li,i_Tooley))



print(f"Total Votes: {total}")
print(f"Khan: {format(Khan_percent,'.3f')}% ({i_khan})")
print(f"Correy: {format(Correy_percent,'.3f')}% ({i_Correy})")
print(f"Li: {format(Li_percent,'.3f')}% ({i_Li})")
print(f"O'Tooley: {format(Tooley_percent,'.3f')}% ({i_Tooley})")
print(f"Winner: {max(max_voters,key=max_voters.get)}")




file.write("```text\n")
file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total Votes: {total}\n")
file.write(f"Khan: {format(Khan_percent,'.3f')}% ({i_khan})\n")
file.write(f"Correy: {format(Correy_percent,'.3f')}% ({i_Correy})\n")
file.write(f"Li: {format(Li_percent,'.3f')}% ({i_Li})\n")
file.write(f"O'Tooley: {format(Tooley_percent,'.3f')}% ({i_Tooley})\n")
file.write(f"Winner: {max(max_voters,key=max_voters.get)}\n")