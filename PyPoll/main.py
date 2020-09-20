# importing os module to be able to create file paths through the operating system
import os

# importing csv module to be able to read csv file
import csv

# Creating the path from the current directory to the csv file need to be used
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:

    # Specifying delimiter and variable csvreader to split the data and store it in the variable
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Capturing header from the csv file
    csvheader = next(csvreader)

    # Defining initial value
    TotalVotes = 0
    Candidates = []
    CandidatesVotes = []
    VotePercentage = []
    HighestVote = 0

    # Start looping for each row
    for row in csvreader:
        # Counting total votes since every row is 1 vote
        TotalVotes += 1

        # if the candidate's name is not on the list, add the name to the candidates list and add the number 0 on candidate vote list
        if row[2] not in Candidates:
            Candidates.append(row[2])
            CandidatesVotes.append(0)

        # For each row, add 1 to the candidates chosen for that row    
        CandidatesVotes[Candidates.index(row[2])] += 1
    
    # For loop to calculate percentage as well as determining winner
    for percentrow in CandidatesVotes:
        VotePercent = percentrow * 100 / TotalVotes
        VotePercentage.append(round(VotePercent,3)) 
        if(percentrow > HighestVote):
            Winner = Candidates[CandidatesVotes.index(percentrow)]
            HighestVote = percentrow
    
    # Printing to terminal
    #===========================================
    print(f'''
Election Results
----------------------------
Total Votes: {TotalVotes}
----------------------------''')
    for index in range(len(Candidates)):
        formattedPercent = format(VotePercentage[index],'.3f')
        print(f"{Candidates[index]}: {formattedPercent}% ({CandidatesVotes[index]})")
    print(f'''----------------------------
Winner: {Winner}
----------------------------''')
    #=============================================

    # Printing to text file
    txtpath = os.path.join('analysis', 'PyPollAnalysis.txt')
    with open(txtpath, "w") as text_file:
        print(f'''Election Results
----------------------------
Total Votes: {TotalVotes}
----------------------------''', file = text_file)
        for index in range(len(Candidates)):
            formattedPercent = format(VotePercentage[index],'.3f')
            print(f"{Candidates[index]}: {formattedPercent}% ({CandidatesVotes[index]})",file = text_file)
        print(f'''----------------------------
Winner: {Winner}
----------------------------''',file = text_file)

