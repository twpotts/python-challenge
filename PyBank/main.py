# Import required packages

import os

# Connect to files

input_file = os.path.join(os.getcwd(), "PyBank", "Resources", "budget_data.csv")
output_file = os.path.join(os.getcwd(), "PyBank", "analysis", "analysis.txt")

# Initialize variables

line_count = 0
total_months = 0
total_amount = 0
amounts = []
changes = []
max_month = ""
min_month = ""
max_change = 0
min_change = 0

# Open input file

with open(input_file, "r") as f:

    # Iterate through each line in input file

    for line in f.readlines():
        line_count += 1
        if line_count == 1:
            header_row = line
            continue # The first line is the header line. We can't do calculations on it, so we skip it.
        line_split = line.split(",")
        if len(line_split) < 2:
            print(f"Error: Unexpected line {line}")
            continue # The code below assumes there will be at least 2 results in the line split. If not, we skip it.
        month = line_split[0]
        amount = line_split[1]
        try:
            amount = float(amount)
        except:
            print(f"Error: Unexpected amount {amount}")
            continue # The amount has to something able to be converted to a number. If not, we skip it.
        if len(amounts) > 0: # There needs to be at least one prior amount in order to calculate change.
            change = amount - amounts[-1]
            if change > max_change:
                max_month = month
                max_change = change
            if change < min_change:
                min_month = month
                min_change = change
            changes.append(change)
        amounts.append(amount)
        total_months += 1
        total_amount += amount

    # Close input file

    f.close()

# Calculate summary statistics

avg = round(sum(changes) / len(changes), 2)

# Print in terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${int(round(total_amount,0))}")
print(f"Average Change: ${avg}")
print(f"Greatest Increase in Profits: {max_month} (${int(round(max_change,0))})")
print(f"Greatest Decrease in Profits: {min_month} (${int(round(min_change,0))})")

# Open output text file

with open(output_file, 'w') as output:
    output.write("Financial Analysis" + '\n')
    output.write("----------------------------" + '\n')
    output.write(f"Total Months: {total_months}" + '\n')
    output.write(f"Total: ${int(round(total_amount,0))}" + '\n')
    output.write(f"Average Change: ${round(avg,2)}" + '\n')
    output.write(f"Greatest Increase in Profits: {max_month} (${int(round(max_change,0))})" + '\n')
    output.write(f"Greatest Decrease in Profits: {min_month} (${int(round(min_change,0))})")

    # Close output text file

    output.close()

# END