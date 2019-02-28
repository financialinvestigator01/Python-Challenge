# PyBank problem
import os
import csv

# Point to and read budget_data.csv from Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #skip the header row

    # initialize variables and perform calculations
    counter = 0
    net_profit_loss = 0
    firstrow = True
    GreatestProfitIncrease = 0
    GreatestLossDecrease = 0
    holder = 0


    for row in csvreader:
        counter += 1 # Calculate the total number of months in the dataset
        net_profit_loss += float(row[1]) # Calculate the net total amount of "Profit/Losses" over the entire period
        if firstrow:
            firstpl = float(row[1]) #initialize the first value in the list
            firstrow = False
        lastpl = float(row[1]) #initialize the last value in the list
        
        month = row[0] # month placeholder
        amount = row[1] # amount placeholder
        rowamount = float(amount)
        difference = rowamount - holder
        if GreatestProfitIncrease < difference: # Calculate the greatest increase in profits (date and amount) over the entire period
            GreatestProfitIncrease = difference
            GreatestProfitIncrease_month = month
        
        if GreatestLossDecrease > difference: # Calculate the greatest decrease in losses (date and amount) over the entire period
            GreatestLossDecrease = difference
            GreatestLossDecrease_month = month
        
        holder = rowamount
  
    average_change_PL = float( (lastpl - firstpl) / (counter -1) ) # Calculate the average of the changes in "Profit/Losses" over the entire period
    average_change_PL = round(average_change_PL, 2)

    print(f"Financial Analysis") # output to terminal
    print(f"----------------------------------") # output to terminal
    print(f"Total Months: {counter}") # output to terminal
    print(f"Net Profit/Loss: ${net_profit_loss}") # output to terminal
    print(f"Average of changes in Profit/Losses: ${average_change_PL}") #output to terminal
    print(f"Greatest Increase in Profits: {GreatestProfitIncrease_month}: (${GreatestProfitIncrease})") #output to terminal
    print(f"Greatest Decrease in Profits: {GreatestLossDecrease_month}: (${GreatestLossDecrease})") #output to terminal


    # what file to write to
    FinancialAnalysis_output = os.path.join("financial_analysis_output.txt")

    with open(FinancialAnalysis_output, 'w', newline='') as textfile:
        textfile.write("Financial Analysis" + os.linesep)
        textfile.write("--------------------------------" + os.linesep)
        textfile.write("Total Months: %s" % counter + os.linesep)
        textfile.write("Net Profit/Loss: %s" % net_profit_loss + os.linesep)
        textfile.write("Average of changes in Profit/Losses: %s" % average_change_PL + os.linesep)
        textfile.write("Greatest Increase in Profits: %s" % GreatestProfitIncrease_month + ": %s" % GreatestProfitIncrease + os.linesep)
        textfile.write("Greatest Decrease in Profits: %s" % GreatestLossDecrease_month + ": %s" % GreatestLossDecrease + os.linesep)
                
        #print(f"Financial Analysis\n", file=textfile) # output to textfile
        #print(f"----------------------------------\n", file=textfile) # output to textfile    
        #print(f"Total Months: {counter}\n", file=textfile)# output to textfile        
        #print(f"Net Profit/Loss: ${net_profit_loss}\n", file=textfile) # output to textfile        
        #print(f"Average of changes in Profit/Losses: ${average_change_PL}\n", file=textfile) #output to textfile        
        #print(f"Greatest Increase in Profits: {GreatestProfitIncrease_month}: (${GreatestProfitIncrease})\n", file=textfile) #output to textfile        
        #print(f"Greatest Decrease in Profits: {GreatestLossDecrease_month}: (${GreatestLossDecrease})\n", file=textfile) #output to textfile




# your analysis should look similar to the one below:
#     Financial Analysis
#     ----------------------------
#     Total Months: 86
#     Total: $38382578
#     Average  Change: $-2315.12
#     Greatest Increase in Profits: Feb-2012 ($1926159)
#     Greatest Decrease in Profits: Sep-2013 ($-2196167)
# Print final results to the terminal and a new file
