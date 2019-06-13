# Create a Python script that analyzes the votes and calculates each of the following:
# -->>  The total number of votes cast
# -->>  A complete list of candidates who received votes
# -->>  The percentage of votes each candidate won
# -->>  The total number of votes each candidate won
# -->>  The winner of the election based on popular vote


# Import dependencies
import os
import csv
import collections
from collections import Counter

# Define PyPoll's variables
voters_candidates = []
votes_per_candidate = []

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    #print(f"Header: {csv_header}")
    # This prints -->> Header: Voter ID,Country,Candidate
    # Read through each row of data after the header
    for row in csv_reader:

        voters_candidates.append(row[2])

    # Sort the list by default ascending order
    sorted_list = sorted(voters_candidates)

    #sorted_list = sorted(voters_candidates, reverse=True) 
    #sorted_list.sort(reverse=True) 

    #for key, group in groupby(sorted_list):
    
    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    #count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # calculate the percentage of votes per candicate in 3 digital points
    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
          
    #print(c.most_common())
    #print(c.values())
    #print(c.keys())
    #print(sum(c.values()))
    
# -->>  Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


# -->>  Export a text file with the results
election_file = os.path.join("Output", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    outfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    outfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    outfile.write(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    outfile.write("-------------------------\n")    
   