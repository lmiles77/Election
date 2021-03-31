# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join( "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Resources", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# 2: Track the largest county and county voter turnout.
largest_county = ""
county_voter = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    # Read the header
    headers = next(file_reader)

    # For each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # 3: Extract the county name from each row.
        county_name = row[1]
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:
           county_options.append(county_name)
            # 4c: Begin tracking the county's vote count.
        county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
     # Print the final vote count (to terminal)
     election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
print(election_results, end="")
   
# 6a: Write a for loop to get the county from the county dictionary.
for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]

    # 6c: Calculate the percentage of votes for the county.
vote_percentage = float(votes) / float(total_votes) * 100
county_results = (
    f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
     # 6d: Print the county results to the terminal.
print(county_results)    

    #  6e: Save the candidate results to our text file.
txt_file.write(candidate_results)

    # 6f: Write an if statement to determine the winning county and get its vote count.
     # Determine winning vote count, winning percentage, and winning candidate.
if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_county = county_name
            winning_percentage = vote_percentage


    # 7: Print the county with the largest turnout to the terminal.
print(winning_county)

    # 8: Save the county with the largest turnout to a text file.
txt_file.write(winning_county_summary)
    

print(candidate_results)
    #  Save the candidate results to our text file.
txt_file.write(county_results)


