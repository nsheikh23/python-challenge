#!/usr/bin/env python
# coding: utf-8

# Pypoll Election Analysis
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
analysis = os.path.join("analysis", "Analysis.txt")

total_votes = 0
cand_dict = {}
unique_lst =[]
pct_lst = []

# Opening the CSV file
with open(csvpath) as csvfile:
    fieldnames = ["Voter ID", "County", "Candidate"]
    csvreader = csv.DictReader(csvfile, fieldnames = fieldnames, delimiter=',')
    
# # Skipping the header row
# # Able to print it out if needed
    csvheader=next(csvreader)
# #     print(f"CSV Header: {csvheader}")


# # Looping through each row of the CSV file
# # ABle to print out all the rows if needed
    
    for row in csvreader:
#         print(row)
        total_votes += 1
    
#     After getting total votes, begin by adding candidate to the unique list and candidate dictionary
#     If the candidate is already on the list then update the values in the dictionary for the candidate/key
        if row["Candidate"] not in unique_lst:
            unique_lst.append(row["Candidate"])
            cand_dict[row["Candidate"]] = 0
        
        cand_dict[row["Candidate"]] += 1
    
    #         Finding the most votes
        count = max(cand_dict.values())
        
#         Iterating through the dictionary to find the candidate associated with the most votes
        for key,value in cand_dict.items():
            if count == value:
                winner = key
                
    
    print(f"Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-----------------------------")
    #     Calculate the percentage of each candidate in the dictionary
    for candidate,count in cand_dict.items():
        pct = count/total_votes *100
        print(f"{candidate}: {pct:.3f}% ({count})")     
    print(f"-----------------------------")
    print(f"Winner: {winner}")
    print(f"-----------------------------")
    
#  Opening new file where to write the results of the function
with open(analysis, 'w') as newFile:

#             Writing the following lines in the text file
    newFile.write("Election Results\n")
    newFile.write("-----------------------------\n")
    for candidate,count in cand_dict.items():
        pct = count/total_votes *100
        newFile.write(f"{candidate}: {pct:.3f}% ({count})\n")     
    newFile.write(f"-----------------------------\n")
    newFile.write(f"Winner: {winner}\n")
    newFile.write(f"-----------------------------\n")