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
    for row in csvreader:
        counter = counter + 1 # Calculate the total number of months in the dataset
        net_profit_loss = float(row[1]) + (float(net_profit_loss)) # Calculate the net total amount of "Profit/Losses" over the entire period
        
     
    print("Total Months: ", counter)
    print("Net Profit/Loss: $", net_profit_loss)


# Calculate the average of the changes in "Profit/Losses" over the entire period
# Calculate the greatest increase in profits (date and amount) over the entire period
# Calculate the greatest decrease in losses (date and amount) over the entire period
# your analysis should look similar to the one below:
#     Financial Analysis
#     ----------------------------
#     Total Months: 86
#     Total: $38382578
#     Average  Change: $-2315.12
#     Greatest Increase in Profits: Feb-2012 ($1926159)
#     Greatest Decrease in Profits: Sep-2013 ($-2196167)
# Print final results to the terminal and a new file
