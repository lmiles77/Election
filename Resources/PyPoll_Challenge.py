# Add our dependencies.
import csv
import os
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_results.txt")
# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
candidate_name = ""

# Create a list and count votes dictionary.
county_options = []
county_votes = {}

# Track largest county, vote county, and percentage.
largest_county_turnout = ""
largest_percentage = 0
largest_count = 0
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    header = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        county_name = row[1]
        # Get the county name from each roew.
        candidate_name = row[2]       

        # county does not match any existing county in the county list.
        if county_name not in county_options:
            # Add the candidate name to the candidate list.
            county_options.append(county_name)
            # And begin tracking that candidate's voter count.
            county_votes[county_name] = 0
        # Add a vote to that candidate's count
        county_votes[county_name] += 1

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Save the final vote count to the text file. 

# Save results to text file.
with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.   
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")                                             
    print(election_results, end="") 
    txt_file.write(election_results)

    # Save county results to the text file.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100 
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)

        # Write if statement to determine largest county turnout.
        if (votes > largest_count) and (vote_percentage > largest_percentage):
            largest_count = votes
            largest_county_turnout = county_name
            largest_percentage = vote_percentage

           # Print the winning candidate's results to the terminal.
        largest_county_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {largest_county_turnout}\n"
            f"-------------------------\n")
    print(largest_county_summary)
            # Save the winning candidate's results to the text file.
    txt_file.write(largest_county_summary)
    
    # Save candidate results to text file.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes    
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)













     
        








   