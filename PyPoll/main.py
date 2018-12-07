import os
import csv
# ---------------------------------------------------------------------------------------
csvpath = os.path.join("election_data.csv")  # read in file from same directory
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    list_csv = list(csvreader)

    Rows = int(len(list_csv))  # count the number of rows in the data file
    num_votes = Rows - 1  # subtract 1 from Rows if there is a header equal to no. of votes

# ---------------------------------------------------------------------------------------
# Lists the unique candidate names in list Candidates

    Candidates = []
    name = str()
    for i in range(1,Rows):
        name = str(list_csv[i][2])
        if name not in Candidates:
            Candidates.append(name)

    No_Candidates = int(len(Candidates))  # Calculates the number of Candidates

# ---------------------------------------------------------------------------------------
# Calculates the number of votes each candidate received in list Candidates

    count = [0]*(len(Candidates))

    for j in range(1, Rows):
        for k in range(0, int(len(Candidates))):
            if str(list_csv[j][2]) == (Candidates[k]):
                count[k] = count[k] + 1

# ---------------------------------------------------------------------------------------
# Calculates the percentage of total votes each candidate received in list Percent

    Percent = [0]*(len(Candidates))
    for n in range(0, int(len(Candidates))):
        Percent[n] = round(((count[n]/num_votes) * 100), 2)

# ---------------------------------------------------------------------------------------
# Calculates the winner according to most votes (biggest percentage)

    Most = 0
    Winner = []
    for p in range(0, int(len(Candidates))):
        if int(count[p]) > Most:
            Winner = Candidates[p]
            Most = int(count[p])

# ---------------------------------------------------------------------------------------

print("Election Results")
print("------------------------------")
print("Total Votes: " + str(num_votes))
print("------------------------------")
for s in range(0, int(len(Candidates))):
    print(str(Candidates[s])+": " + str(Percent[s]) + "%" + "(" + str(count[s]) + ")")
print("------------------------------")
print("Winner is: " + Winner)
print("------------------------------")

# ---------------------------------------------------------------------------------------

f = open('Pypoll-output.txt', 'w')

print("Election Results", file=f)
print("------------------------------", file=f)
print("Total Votes: " + str(num_votes), file=f)
print("------------------------------", file=f)
for s in range(0, int(len(Candidates))):
    print(str(Candidates[s]) + ": " + str(Percent[s]) + "%" + "(" + str(count[s]) + ")", file=f)
print("------------------------------", file=f)
print("Winner is: " + Winner, file=f)
print("------------------------------", file=f)

f.close()
