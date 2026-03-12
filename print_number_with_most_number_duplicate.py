# A dictionary to store the number as a 'key' and its count as the 'value'
frequency_map = {}

print("Enter numbers (type 'stop' to finish):")
while True:
    try:
        user_input = input("> ")
        num = float(user_input)

        # If number exists, add 1 to its count; otherwise, start at 1
        frequency_map[num] = frequency_map.get(num, 0) + 1
    except ValueError:
        # Exit the loop if input is not a valid number
        break

if frequency_map:
    # max() looks through the dictionary to find the key with the highest value
    most_frequent = max(frequency_map, key=frequency_map.get)
    print(f"The number {most_frequent} had the most duplicates.")