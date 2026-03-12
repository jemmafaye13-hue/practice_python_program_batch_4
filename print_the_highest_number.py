highest = None # Initialize as None to handle the first input correctly

print("Enter numbers (input letter to stop):")
while True:
    try:
        num = float(input("> "))
        # Update 'highest' if it's the first number OR if new number is larger
        if highest is None or num > highest:
            highest = num
    except ValueError:
        break

if highest is not None:
    print(f"The highest value recorded was: {highest}")