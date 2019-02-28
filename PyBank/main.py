import os
import csv
budgetcsv = os.path.join ("budget_data.csv")

def unique():

    rows = list(csv.reader(open('budget_data.csv', 'r'), delimiter=','))

    result = []

    for r in rows:
        key = r
        if key not in result:
            result.append(r)
    return result
# Define function
#def profitloss(pnldata):
# The total number of months included in the dataset
#  row_count = sum(1 for row in csvreader)
# The net total amount of "Profit/Losses" over the entire period
 #  total = 0
  # for row in csvreader:
   #    total += float(row[1])

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# Print results
   #print(row_count)
   #print (total)
   # # Read in file and split the data
# with open(budgetcsv, 'r') as csvfile:
#  csvreader = csv.reader(csvfile, delimiter=',')
  # next(csvreader)
# Loop through data
#   for row in csvreader:
#       profitloss(row)