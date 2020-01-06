#Import to read csv files

import os
import csv



# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Gets the header of the file
    header = next(csvreader)
    election_data = list(csvreader)

    #Creating lists that I'll later combine for my summary
    Candidate = []
    Percent = []
    Votes = []


    #Initializing variables I'll use for the total votes of each candidate
    total = 0
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0

    #Initializing variables I'll use for the percentages
    percent1 = 0.0
    percent2 = 0.0
    percent3 = 0.0
    percent4 = 0.0

    #Getting the total amount of votes using the length 
    total = (len(election_data))

    #Filling Candidate list with the names from the file 
    for row in election_data:
        Candidate.append(row[2])
        
    #Using set to get the unique candidates in the list
    Names = set(Candidate)

    #Sorting the file so the list new can be static and not change every time the code is ran
    new = sorted(Names) 
     

    

    #Getting the total votes for each candidate. Can probably do more with this loop.
    for row in election_data:
        if row[2] == new[0]:
            total1 += 1
        if row[2] == new[1]:
            total2 += 1
        if row[2] == new[2]:
            total3 += 1
        if row[2] == new[3]:
            total4 += 1

    #Getting the percent of the vote. I'm sure this could have went into a loop
    percent1 = total1 / total
    percent2 = total2 / total
    percent3 = total3 / total
    percent4 = total4 / total
    

    #Creating lists to combine for the summary
    Candidate = [new[0], new[1], new[2], new[3]]
    Percent = [percent1, percent2, percent3, percent4]
    Votes = [total1, total2, total3, total4]
    
    #Combining the lists into one list
    election_sum = zip(Candidate, Percent, Votes)
    election_sum = list(election_sum)

    #Creating a dictionary to get the winner
    winner = zip(Candidate, Percent)
    winner = dict(winner)
    
    #Using max to find the winner value and key
    MV = max(winner.values())
    MN = max(winner, key=lambda key: winner[key])
    
    
    #Terminal print out
    print("```text")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total}")
    print("-------------------------")
    print(election_sum[1][0], "{:.3%}".format(election_sum[1][1]), election_sum[1][2])
    print(election_sum[0][0], "{:.3%}".format(election_sum[0][1]), election_sum[0][2])
    print(election_sum[2][0], "{:.3%}".format(election_sum[2][1]), election_sum[2][2])
    print(election_sum[3][0], "{:.3%}".format(election_sum[3][1]), election_sum[3][2])
    print("-------------------------")
    print(f"Winner: {MN}")
    print("-------------------------")
    print("```")
    
#Writing the summary to a text file.
with open("Election_Summary.txt", "w") as summary:
    summary.write("```text\n")
    summary.write("ElectionResults\n")
    summary.write("-------------------------\n")
    summary.write(f"TotalVotes:{total}\n")
    summary.write("-------------------------\n")
    print(election_sum[1][0], "{:.3%}".format(election_sum[1][1]), election_sum[1][2], file=summary)
    print(election_sum[0][0],  "{:.3%}".format(election_sum[0][1]), election_sum[0][2], file=summary)
    print(election_sum[2][0],  "{:.3%}".format(election_sum[2][1]), election_sum[2][2], file=summary)
    print(election_sum[3][0], "{:.3%}".format(election_sum[3][1]), election_sum[3][2], file=summary)
    summary.write("-------------------------\n")
    summary.write(f"Winner:{MN}\n")
    summary.write("-------------------------\n")
    summary.write("```")

  