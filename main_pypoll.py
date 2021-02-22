# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 11:51:04 2021

@author: Jenkir
"""

import os

# Module for reading CSV files
import csv


csvpath = os.path.join('Resources/election_data.csv')
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
print(csvreader)


total_votes  = 0

#temp amount used to store previous month profit/loss
temp_amount = 0
#changes is a list where we will put monthly changes
changes = []

change = 0
max_change = ["", -999999]
min_change = ["", 999999]


#     print(csvreader)

#     # Read the header row first (skip this step if there is no header)
#     csv_header = next(csvreader)
#    
#     # Read each row of data after the header
for row in csvreader:
#         total_votes = total_votes + 1

    print(total_votes)
#         total_profit_loss = total_profit_loss + int(row[1])
#         change = int(row[1]) - temp_amount
#         if row[0] != "Jan-2010":
#             changes.append(change)
#             if change > max_change[1]:
#                 max_change = [row[0], change]
#             if change < min_change[1]:
#                 min_change = [row[0], change]
               
#         temp_amount = int(row[1])
# print("Election Results")              
# print(total_votes)
# print(total_profit_loss)
# print(changes)
# print(mean(changes))
# print(max_change)
# print(min_change)
    

        
