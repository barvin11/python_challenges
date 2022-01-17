import os
import csv

#Defining the path
csvpath = os.path.join("Resources","election_data.csv")

# variables for measure - need to move into a vote count list

count = 0
cand = []
uniqcand = []

khanvote = 0
correyvote = 0
livote = 0
otooleyvote = 0

votetally = [khanvote,correyvote,livote,otooleyvote]


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader:
        count += 1             #Pull together the list of candidates
        cand.append(row[2])

for name in cand:  
    if name not in uniq_cand:
        uniq_cand.append(name)
    elif name == 'Khan':
        khanvote += 1
    elif name == 'Correy':
        correyvote += 1
    elif name == 'Li':
        livote += 1                      
    else otooleyvote += 1
    
winningcount = max(votetally)
    
winner = uniqcand[votetally.index(winningcount)]

print(uniqcand)
print(count)
print(khanvote)
print(correyvote)
print(livote)
print(otooleyvote)
print(winner)

print("Election Results")
print("--------------------")
print(f"Total Votes: {count}")
print("--------------------")  
print(f"Khan: {round((khanvote/count)*100, 2)}% ({khanvote})")
print(f"Correy: {round((correyvote/count)*100, 2)}% ({correyvote})")
print(f"Li: {round((Livote/count)*100, 2)}% ({Livote})")
print(f"O'Tooley: {round((otooleyvote/count)*100, 2)}% ({otooleyvote})")







