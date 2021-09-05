import csv
import os

file_to_load = 'C:/Users/slash/Documents/Election_Annalysis/resources/election_results.csv'
#Vote Counter
total_Votes=0

#Candidate List
candidate_options=[]

#candidate Votes
candidate_votes = {}
votes=candidate_votes

#percentage calculated
#vote_percentage = (votes / total_Votes) * 100

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Assign a variable for the file to load and the path.
file_to_load = os.path.join( "Resources","election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:


# Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("----------------\n")
    txt_file.write("Arapahoe,\n")
    txt_file.write("Denver,\n")
    txt_file.write("Jefferson,\n")
# Close the file
# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_Votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # Save the results to our text file.
    
    with open(file_to_save, "w") as txt_file:
    # Determine the percentage of votes for each candidate by looping through the counts.
        # Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_Votes) * 100

            #  To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.

            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
            winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
            # Print the final vote count to the terminal.
            election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_Votes:,}\n"
            f"-------------------------\n")
            print(election_results, end="")
            # Save the final vote count to the text file.
            txt_file.write(election_results)
#print(winning_candidate_summary)
#  To do: print out the winning candidate, vote count and percentage to
#   terminal.

    

# Print the candidate list.
#print(candidate_options)
#print candidate votes dictionary
print(candidate_votes)


