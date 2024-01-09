import os
import pandas as pd

# Get the absolute path of the script
script_path = os.path.abspath(__file__)

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(script_path))

# Construct the absolute path for 'election_data.csv'
file_path = os.path.join('Resources', 'election_data.csv')

# Construct the full path for the output text file
output_file_path = os.path.join('analysis', 'output.txt')

# Ensure the 'analysis' folder exists
analysis_folder = os.path.join(os.path.dirname(script_path), 'analysis')
if not os.path.exists(analysis_folder):
    os.makedirs(analysis_folder)

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Calculate the total number of votes cast
total_votes = len(df)

# Create a list of unique candidates who received votes
candidates = df["Candidate"].unique()

# Calculate the percentage of votes each candidate won and the total number of votes each candidate won
candidate_votes = df["Candidate"].value_counts()
candidate_percentages = candidate_votes / total_votes * 100

# Find the winner based on popular vote
winner = candidate_votes.idxmax()

# Prepare the analysis results
analysis_results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate in candidates:
    analysis_results += f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n"

analysis_results += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------"
)

# Print the results to the terminal
print(analysis_results)

# Export the results to the specified text file path
with open(output_file_path, 'w') as txtfile:
    txtfile.write(analysis_results)
