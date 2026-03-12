running_total = 0
count = 0

print("Enter numbers (input letter to calculate average):")
while True:
    try:
        num = float(input("> "))
        running_total += num  # Add the number to the sum
        count += 1            # Keep track of how many numbers were entered
    except ValueError:
        break

# Avoid "Division by Zero" error if user stops immediately
if count > 0:
    average = running_total / count
    print(f"The average of the {count} numbers is: {average}")
else:
    print("No data to calculate.")