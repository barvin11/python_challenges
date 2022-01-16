import os

import pandas as pd

#dates = [] #list of months
#sums = [] #list of months
#diffs = [] #list of P&L differences

csvpath = os.path.join("Resources","budget_data.csv")
# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile,delimiter=',')
    
#     csvheader = next(csvreader)

#     for row in csvreader:
#         #row = [Date, Profit/Losses]
#         #date = float(row[0])
#         #pl = float([1])
#         #print(row)
#         dates.append(row[0])
#         sums.append(row[1])
#         #diffs.append(row[2])

#         print(f'[{csvreader.index(row)}] {row}')

#      budget = zip(dates,sums,diffs)
#  with open("analysis/pl", "w") as textfile:
#      writer = csv.writer (new_file)
#      writer.writerow(["dates","sums","diffs"])
#      writer.writerows(budget)

headers = ["Date","Profit/Losses"]
df = pd.read_csv(csvpath,usecols=headers)
months = df["Date"].count()                     #Count of Months
pl = df["Profit/Losses"].sum()                  #Sum of Monthly P&Ls
pldiffs = df["Profit/Losses"].diff().mean()     #Average Monthly P&Ls
Maxinc = df["Profit/Losses"].diff().max()       #
Mininc = df["Profit/Losses"].diff().min()       #
Maxloc = df["Profit/Losses"].max()
Minloc = df["Profit/Losses"].min()
Maxloc = df.loc[df["Profit/Losses"] == Maxloc, "Date"]
Maxincdateloc = Maxloc.iloc[0]
Minloc = df.loc[df["Profit/Losses"] == Minloc, "Date"]
Minincdateloc = Minloc.iloc[0]
#print(Maxincdateloc)


  
with open("analysis/pl", "w") as textfile:
    textfile.write('Financial Analysis'+'\n')
    textfile.write('------------------------------'+'\n')
    textfile.write(f'Total Months:{months}'+'\n')
    textfile.write(f'Total:{pl}'+'\n')
    textfile.write(f'Average Change:{pldiffs}'+'\n')
    textfile.write(f'Greatest Increase in Profits:{Maxinc}'+'\n')
    textfile.write(f'Greatest Decrease in Profits:{Mininc}'+'\n')
     #writer.writerow(["dates","sums","diffs"])
     #writer.writerows(budget)