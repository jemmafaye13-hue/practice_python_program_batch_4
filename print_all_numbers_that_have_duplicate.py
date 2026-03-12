# Create an empty list to store the 10 user inputs
numbers = []

# Loop 10 times to collect input
for i in range(10):
    val = float(input(f"Enter number {i+1}: "))
    numbers.append(val)

# Create a 'set' to store unique instances of duplicates (prevents printing the same duplicate twice)
duplicates = set()

for x in numbers:
    # count() checks how many times 'x' appears in the list
    if numbers.count(x) > 1:
        duplicates.add(x)

print("Numbers that appeared more than once:", duplicates)