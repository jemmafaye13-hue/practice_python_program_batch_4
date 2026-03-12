data_list = []

while True:
    try:
        val = float(input("Enter number (any letter to sort): "))
        data_list.append(val)
    except ValueError:
        break

# sort() organizes the list. reverse=True flips it from Ascending to Descending
data_list.sort(reverse=True)
print("List from highest to lowest:", data_list)