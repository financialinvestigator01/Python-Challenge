# Your task is to create a Python script that analyzes the votes and calculates each of the following:

import os
import csv


# Point to and read election_data.csv from Resources folder
csvpath = os.path.join('Resources', 'Book1.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #skip the header row

    # file contains Voter ID, County, Candidate columns
    # initialize variables and initial conditions
       
    numberholder = 0
    candidate_dict = {} # creates an empty dictionary, will be used
                        # to hold the candidate names as keys, and number of votes
                        # as values

    for row in csvreader:
        numberholder += 1 # The total number of votes cast
        if (row[2] in candidate_dict):      # checks to see if a candidate has been
            candidate_dict[row[2]] += 1     # voted for yet. If yes, keeps a running
        else:                               # total.
            candidate_dict[row[2]] = 1      # if not, adds the new candidate to the 
                                            # dictionary with 1 vote.

             
# new for loop to determine winner
     


print("values: ", candidate_dict)

#    A complete list of candidates who received votes

#    The percentage of votes each candidate won

#    The total number of votes each candidate won

#    The winner of the election based on popular vote.


print("Election Results")
print("------------------------------")
print("Total number of votes: ", numberholder)
print("------------------------------")


# As an example, your analysis should look similar to the one below:

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
