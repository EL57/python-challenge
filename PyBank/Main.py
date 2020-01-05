#Import to read csv files

import os
import csv



# Path to collect data from the Resources folder
pybank_csv = os.path.join('Resources', 'budget_data.csv')

#list to store data
Date = []
Profit_loss = []
Change = []


# Read in the CSV file
with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #writer = csv.writer(open('pybankNew.csv', 'w'))
  

    #Gets the header of the file
    header = next(csvreader)
    bank_data = list(csvreader)
    
    #Printing the header so I can see if the 'Change' column is there
    #print(header)

    #initiating variables I may or may not need
    count = 0 #len(bank_data)
    total = 0
    bd = 0
   
    #Reads through the rows in th csv file
    for row in bank_data:
        count += 1
        total += int(row[1])
        #bd = int(bank_data[count][1]) - int(bank_data[count-1][1])
        #row.append(bd)
        #writer.writerow(bank_data)
        Date.append(row[0])
        Profit_loss.append(row[1])
        
        #print(row)
    
    #Creating a list from the bank_data to get the average of the price changes
    new = [int(bank_data[i+1][1]) - int(bank_data[i][1]) for i in range(len(bank_data) - 1)]
    row.append(new)
    
    
    #Inserting a zero in the first row to make the column even for future appends
    new.insert(0,0)
    
    #Averaging the "new" list. Subtracting 1 from the length to get the right average
    avg = sum(new) / (len(new)-1) 

    #Combining lists to create a dictionary
    good_csv = zip(Date, new)
    
    # converting values to print as a dictionary so I can find the max and min 
    good_csv = dict(good_csv)
    
    #Getting the key and value so I can put the $ in front of the amount
    MA = max(good_csv.values())
    MA2 = max(good_csv, key=lambda key: good_csv[key])

    mi = min(good_csv.values())
    mi2 = min(good_csv, key=lambda key: good_csv[key])

    #Variables to get the max and min 
   # MA = max(good_csv.items(), key = lambda x: x[1])
   # mi = min(good_csv.items(), key = lambda x: x[1])


#Defining a function that outputs the summary
def FinancialAnalysis():
    print("```text")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(bank_data)}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round(avg,2)}")
    print(f"Greatest Increase in Profits: {MA2} (${MA})")
    print(f"Greatest Decrease in Profits: {mi2} (${mi})")
    print("```")

#Printing the function
FinancialAnalysis()

#Writing the summary to a text file the old fashioned way since I couldn't write the function
with open("Summary.txt", "w") as summary:
    summary.write("```text\n")
    summary.write("----------------------------\n")
    summary.write(f"Total Months: {len(bank_data)}\n")
    summary.write(f"Total: ${total}\n")
    summary.write(f"Average Change: ${round(avg,2)}\n")
    summary.write(f"Greatest Increase in Profits: {MA2} (${MA})\n")
    summary.write(f"Greatest Decrease in Profits: {mi2} (${mi})\n")
    summary.write("```")
   