# Exercise 13: Print multiplication table from 1 to 10

# pseudocode


# create  outer loop for rows (1 to 10)
# create Inner loop for columns (1 to 10)
# Calculate the product of i and j
# Print the result with adjusted width for proper alignment


# _______________________________ actual code _________________________________________________

# create  outer loop for rows (1 to 10)
for i in range(1, 11):
    # create Inner loop for columns (1 to 10)
    for j in range(1, 11):
        # Calculate the product of i and j
        result = i * j
        # Print the result with adjusted width for proper alignment
        print(f"{result:3}", end=" ")
        
    # Move to the next line after printing a row
    print()