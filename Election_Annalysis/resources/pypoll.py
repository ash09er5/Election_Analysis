

# Assign a variable for the file to load and the path.
file_to_load = 'C:/Users/slash/Documents/Election_Annalysis/resources/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')


# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
# Close the file.
election_data.close()