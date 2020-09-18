# importing os module to be able to create file paths through the operating system
import os

# importing csv module to be able to read csv file
import csv

# Creating the path from current directory to point to the csv file we are going to use
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:

    # Specifying deliminiter and variable csvreader to hold the content of the file
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Capturing the header from the csv file
    csvheader = next(csvreader)

    # As every entry is for each month, the length of the array will be the total months
    # numofmonth = len(list(csvreader))

    Total = 0
    numofmonth = 0

    for row in csvreader:
        Total = Total + int(row[1])
        numofmonth += 1

    print(Total)
    print(numofmonth)
    
