#!/usr/bin/env python
# coding: utf-8

# Pybank Financial Analysis
import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
analysis = os.path.join('analysis', 'Analysis.txt')

# Declare variables and lists
count = 0
months = []
revenue = []
prev_rev = 0
chg_lst =[]


# Opening the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
# Skipping the header row
# Able to print it out if needed
    csvheader=next(csvreader)
#     print(f"CSV Header: {csvheader}")


# Looping through each row of the CSV file
# ABle to print out all the rows if needed
    
    for row in csvreader:
#         print(row)
        
#         Declaring month index in the imported data
#         Appending it to an empty list
        mth_ind= row[0]
        months.append(mth_ind)
        
#         Declaring revenue index in the imported data
#         Appending it to an empty list
        rev_ind= int(row[1])
        revenue.append(rev_ind)
        
#         Counting the number of rows/months
        count += 1
    
        if prev_rev != 0:
            chg = rev_ind - int(prev_rev)
            chg_lst.append(chg)
            prev_rev = rev_ind
        else:
            prev_rev = rev_ind
            
#     Summing up the revenue list created through looping  
    total = sum(revenue)
    
#     Calculating the average change    
    avg = round(sum(chg_lst)/len(chg_lst),2)
    
#     Finding the max number in the list
#     Finding the index of the max number
#     Finding the date associated with the same index
    g_inc = max(chg_lst)
    g_inc_index = chg_lst.index(g_inc)
    date1 = months[g_inc_index + 1]
    
#     Finding the min number in the list
#     Finding the index of the min number
#     Finding the date associated with the same index
    g_dec = min(chg_lst)
    g_dec_index = chg_lst.index(g_dec)
    date2 = months[g_dec_index + 1]

    # Printing the analysis to the terminal
    print(f"Financial Analysis")
    print(f"---------------------------")
    print(f"Total Months: {count}")
    print(f"Total Revenue: ${total}")
    print(f"Average Change: ${avg}")
    print(f"The Greatest Increase in Profits: {date1} (${g_inc})")
    print(f"The Greatest Decrease in Profits: {date2} (${g_dec})")
    
    def output():
        
#         Opening new file where to write the results of the function
        with open(analysis, 'w') as newFile:
            
#             Writing the following lines in the text file
            newFile.write("Financial Analysis\n")
            newFile.write("---------------------------\n")

        #     Writing the number of months
            newFile.write(f"Total Months: {count}\n")

        #     Writing the total revenue
            newFile.write(f"Total Revenue: ${total}\n")

        #     Writing the average change
            newFile.write(f"Average Change: ${avg}\n")

#             Writing the greatest increase
            newFile.write(f"The Greatest Increase in Profits: {date1} (${g_inc})\n")

#             Writing the greatest decrease
            newFile.write(f"The Greatest Decrease in Profits: {date2} (${g_dec})\n")

# Calling the output() function
output()





