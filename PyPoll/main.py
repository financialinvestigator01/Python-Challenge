# Your task is to create a Python script that analyzes the votes and calculates each of the following:

import os
import csv


# Point to and read election_data.csv from Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #skip the header row

    # file contains Voter ID, County, Candidate columns
    # initialize variables and initial conditions
       
    votes = 0
    candidate_dict = {} # creates an empty dictionary, will be used
                        # to hold the candidate names as keys, and number of votes
                        # as values

    for row in csvreader:
        votes += 1 # The total number of votes cast
        # A complete list of candidates who received votes
        if (row[2] in candidate_dict):      # checks to see if a candidate has been
            candidate_dict[row[2]] += 1     # voted for yet. If yes, keeps a running
        else:                               # total.
            candidate_dict[row[2]] = 1      # if not, adds the new candidate to the 
                                            # dictionary with 1 vote.






# Print to terminal ####################################
                                                    ####
print("Election Results")                           ####
print("------------------------------")             ####
print("Total number of votes: ", votes)             ####
print("------------------------------")             ####
                                                    ####
# End Print to terminal ################################

Election_Results_output = os.path.join("Election_Results_output.txt")

with open(Election_Results_output, 'w', newline='') as textfile:
    # Print to text file #########################################################
                                                                              ####
    textfile.write("Election Results" + os.linesep)                           ####
    textfile.write("------------------------------" + os.linesep)             ####
    textfile.write("Total number of votes: %d" % votes + os.linesep)         ####
    textfile.write("------------------------------" + os.linesep)             ####
                                                                              ####
# End Print to textfile      #####################################################



winner = 0
winning_candidate = "John"

for key, value in candidate_dict.items():
    percentage_votes = value / votes                            # The percentage of votes each candidate won
    percentage_votes = "{:.3%}".format(percentage_votes)        # Percentage formatting
    print("%s : %s  (""%d"")"%(key,percentage_votes, value))    # correct printing format
    with open(Election_Results_output, 'a', newline='') as textfile:                    # print to text file
        textfile.write("%s : %s  (""%d"")" %(key,percentage_votes, value) + os.linesep) # print to text file
    
    if value >= winner:                                         # The winner of the election based on popular vote.
        winner = value
        winning_candidate = key
    
print("------------------------------")      # print to terminal
print("The winner is: ", winning_candidate)  # print to terminal
print("------------------------------")      # print to terminal

with open(Election_Results_output, 'a', newline='') as textfile:
        textfile.write("------------------------------" + os.linesep)      # print to text file
        textfile.write("The winner is: %s" % winning_candidate + os.linesep)  # print to text file
        textfile.write("------------------------------" + os.linesep)      # print to text file

    

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
