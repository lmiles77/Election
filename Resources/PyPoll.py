# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file
# with open(file_to_load) as election_data:

#     # To do: perform analysis.
#     print(election_data)

# # Close the file.
# election_data.close()

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


    # Write Counties in the Election to the file.
    txt_file.write("Counties in the Election\n")    
    
    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson\n")


#Pseudocode
# Retrieve the data
# Total number of votes cast
# Complete list of candidates who received votes
# Percentage of votes for each candidate
# Total number of votes for each candidate
# Winner of election based on popular vote