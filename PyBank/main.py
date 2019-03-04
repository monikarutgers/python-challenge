# importing required packages
import os
import csv

# creating variables for file location and change to a different file
csvpath = os.path.join('budget_data.csv')

# setting counters to 0 or empty lists
monthCount = 0
totalRev = 0
monthRev = []
change = []
Date= []

# opening the file to read the csv fotmat in a each line as a new line

with open(csvpath, newline='') as csvfile:

# assigning read file to a varaible seperated by a delimiter

   csvreader = csv.reader(csvfile, delimiter=",")
# skip over the header row (row1)

   header = next(csvreader)
# going throug each row, increasing the month by one each time
   
   for row in csvreader:
      monthCount += 1
      totalRev += int(row[1])
      monthRev.append(int(row[1]))
      Date.append(row[0])

monthChange = monthRev
x = monthCount
while x > 1:
   change.append(monthChange[1]-monthChange[0])   
   monthChange.pop(0)
   x-= 1
   avgRevCh = (sum(change)/len(change))
   greatRev = max(change)
   greatMonthPos = change.index(greatRev)
   greatMonth = Date[greatMonthPos+1]
   revDec = min(change)
   revDecPos = change.index(revDec)
   worstMonth = Date[revDecPos +1]

# print to terminal

print("FINANCIAL ANALYSIS")
print("-----------------------------------------")
print("Total Months:  " + str(monthCount))
print("the Total reveune is $ " + str(totalRev))
print("The Average Revenue Change: $ " + str(avgRevCh))
print("The Greatest increase in revenue is " + str(greatRev))
print("The Greatest month is  " + str(greatMonth))
print("The lowest rev is " + str(revDec))
print("The worst month has been  " + str(worstMonth))
   

# making a new file Text

output_file = os.path.join("Financial Analysis.txt")

# printing output to the text file with output in new line

with open(output_file, 'w') as text_file:
   
   text_file.write("Financial Analysis\n")
   text_file.write('------------------------------' +'\n')
   text_file.write("Total Months: "+ str(monthCount) +'\n')
   text_file.write("The Average Revenue Change: $ " + str(avgRevCh)+'\n')
   text_file.write("The Greatest increase in revenue is " + str(greatRev)+'\n')
   text_file.write("The Greatest month is  " + str(greatMonth)+'\n')
   text_file.write("The lowest rev is " + str(revDec)+'\n')
   text_file.write("The worst month has been  " + str(worstMonth))
   text_file.close()
