# importing os module to be able to create file paths through the operating system
import os

# importing csv module to be able to read csv file
import csv


# Print function that can be called to have formatted print based on instruction
def printanalysis(Months, Totalprofit, Averagechange, MaxIncrease, MaxDecrease):
    return f'''    Financial Analysis
    -----------------------------
    Total Months: {Months}
    Total: ${Totalprofit}
    Average Change: ${Averagechange}
    Greatest Increase in Profits: {MaxIncrease[0]} ({MaxIncrease[1]})
    Greatest Decrease in Profits: {MaxDecrease[0]} ({MaxDecrease[1]})
    '''



# Main function
def main():
    # Creating the path from current directory to point to the csv file we are going to use
    csvpath = os.path.join('Resources','budget_data.csv')

    with open(csvpath) as csvfile:

        # Specifying deliminiter and variable csvreader to hold the content of the file
        csvreader = csv.reader(csvfile, delimiter = ',')

        # Capturing the header from the csv file
        csvheader = next(csvreader)


        # Defining initial value to be used
        Total = 0
        numofmonth = 0
        maxchange = 0
        minchange = 0
        changeslist = []

        # start looping through each row
        for row in csvreader:
            # The total is summing all the value on profit/loss column
            Total = Total + int(row[1])

            # Conditional to obtain the changes in profit/losses
            if numofmonth == 0:  # Initial value for the first element in the iteration
                prevnum = int(row[1])
                # maxprofit = row
                # minprofit = row
            else: # Saving the profit/loss change in the changelist array
                profitchange = int(row[1]) - prevnum
                changeslist = changeslist + [profitchange]
                if profitchange > maxchange: # Save the row if the profit change on the iteration is larger than the one that is saved
                    maxlist = [row[0],profitchange]
                    maxchange = profitchange
                if profitchange < minchange: # Save the row if the profit change on the iteration is smaller than the one that is saved
                    minlist = [row[0],profitchange]
                    minchange = profitchange
                prevnum = int(row[1])
            
            # counting the number of month with the loop
            numofmonth += 1

        Average = sum(changeslist)/(numofmonth - 1)
        print(printanalysis(numofmonth,Total,Average,maxlist,minlist))

        txtpath = os.path.join('analysis', 'PyBankAnalysis.txt')
        with open(txtpath,"w") as text_file:
            print(printanalysis(numofmonth,Total,Average,maxlist,minlist), file = text_file)

main()
    
