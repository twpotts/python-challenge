# Import required packages

import os

# Connect to files

input_file = os.path.join(os.getcwd(), "PyPoll", "Resources", "election_data.csv")
output_file = os.path.join(os.getcwd(), "PyPoll", "analysis", "analysis.txt")

# Initialize variables

line_count = 0
total_votes = 0
votes_by_candidate = {}
winner_name = ""
winner_votes = 0

# Open input file

with open(input_file, "r") as f:

    # Iterate through each line in input file

    for line in f.readlines():
        line_count += 1
        if line_count == 1:
            header_row = line
            continue # The first line is the header line. We can't do calculations on it, so we skip it.
        line_split = line.split(",")
        if len(line_split) < 3:
            print(f"Error: Unexpected line {line}")
            continue # The code below assumes there will be at least 3 results in the line split. If not, we skip it.
        ballot_id = line_split[0]
        county = line_split[1]
        candidate = str(line_split[2]).strip() # Calling the strip method eliminates an invisible line break added to the end
        if candidate not in votes_by_candidate:
            votes_by_candidate[candidate] = 1
        else:
            votes_by_candidate[candidate] += 1
        total_votes += 1

    # Close input file

    f.close()

# Print in terminal

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for key, value in votes_by_candidate.items():
    if value > winner_votes:
        winner_votes = value
        winner_name = key
    pct = round(value / total_votes * 100, 3)
    print(f"{key}: {pct}% ({value})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

# Open output text file

with open(output_file, 'w') as output:
    output.write("Election Results" + '\n')
    output.write("-------------------------" + '\n')
    output.write(f"Total Votes: {total_votes}" + '\n')
    output.write("-------------------------" + '\n')
    for key, value in votes_by_candidate.items():
        if value > winner_votes:
            winner_votes = value
            winner_name = key
        pct = round(value / total_votes * 100, 3)
        output.write(f"{key}: {pct}% ({value})" + '\n')
    output.write("-------------------------" + '\n')
    output.write(f"Winner: {winner_name}" + '\n')
    output.write("-------------------------")

    # Close output text file

    output.close()

# END