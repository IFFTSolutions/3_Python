import os
import csv
# ---------------------------------------------------------------------------------------
csvpath = os.path.join("budget_data.csv")  # read in file from same directory

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    list_csv = list(csvreader)

    Rows = int(len(list_csv))  # count the number of rows in the data file

    num_months = Rows - 1  # subtract 1 from Rows if there is a header

# ---------------------------------------------------------------------------------------
    NetAmount = 0 # set the counter to zero before looping through the rows to sum up the profits/losses
    Net_diff = 0
    diff_list = []  # create a diff_list to tabulate the P/L's between the months
    diff = 0

    for i in range(1, Rows):
        NetAmount = NetAmount + int(list_csv[i][1]) # equals Total P/L values

        if i ==1:
            diff = 0
            diff_list.append(diff)  # first month P/L is equal to zero since no previous month to compare with

        elif i >=2:
            diff = int(list_csv[i][1]) - int(list_csv[i-1][1])
            diff_list.append(diff)  # append the diff_list with the calculated P/Ls

        Net_diff = Net_diff + diff  # sums the total net differences for the months
# ---------------------------------------------------------------------------------------

    AvChange = round((int(Net_diff) / (int(num_months) - 1)), 2)  # Total Net_diff divided by num_months


# ---------------------------------------------------------------------------------------
#  Calculates the biggest increase in profit and corresponding month

    max_pos = diff_list[0]
    pos_month = str()

    for j in range(0, Rows-1):
        if diff_list[j] > max_pos:
            pos_month = str(list_csv[j+1][0])
            max_pos = int(diff_list[j])

# ---------------------------------------------------------------------------------------
#  Calculates the greatest decrease in profit and corresponding month

    max_loss = diff_list[0]
    neg_month = str()

    for j in range(0, Rows-1):
        if diff_list[j] < max_loss:
            neg_month = str(list_csv[j+1][0])
            max_loss = int(diff_list[j])


# ---------------------------------------------------------------------------------------

print("--------------------------------------")
print("Financial Analysis:")
print("--------------------------------------")
print("Total Months: " + str(num_months))
print("Total: $" + str(NetAmount))
print("Average Change: $" + str(AvChange))
print("Greatest Increase in Profits: " + str(pos_month) + " $ " + "(" + str(max_pos) + ")")
print("Greatest Decrease in Profits: " + str(neg_month) + " $ " + "(" + str(max_loss) + ")")

# ---------------------------------------------------------------------------------------

f = open('PyBank-output.txt', 'w')
print("--------------------------------------", file=f)
print("Financial Analysis:", file = f)
print("--------------------------------------", file=f)
print("Total Months: " + str(num_months), file=f)
print("Total: $" + str(NetAmount), file=f)
print("Average Change: $" + str(AvChange), file=f)
print("Greatest Increase in Profits: " + str(pos_month) + " $ " + "(" + str(max_pos) + ")", file=f)
print("Greatest Decrease in Profits: " + str(neg_month) + " $ " + "(" + str(max_loss) + ")", file=f)
f.close()




