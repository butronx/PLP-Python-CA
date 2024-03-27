# mpty list called my_list
my_list = []

# Append elements to my_list: 10, 20, 30, 40.
# Changing the order to "30, 10, 40, 20" is to later demonstrate
# how the sort function works.
my_list.append(30)
my_list.append(10)
my_list.append(40)
my_list.append(20)

# Print current state of my_list
print(f"Current state of my list 1: {my_list}")

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)

# Print current state of my_list
print(f"Current state of my list 2: {my_list}")

# Extend my_list with another list: my_list2 = [50, 60, 70]

my_list2 = [50, 60, 70]
my_list.extend(my_list2)

# Print current state of my_list
print(f"Current state of my list 3: {my_list}")

# Remove the last element from my_list
my_list.pop()

# Print current state of my_list
print(f"Current state of my list 4: {my_list}")

# Sort my_list in ascending order
my_list.sort()

# Print current state of my_list
print(f"Current state of my list 5: {my_list}")

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"Index of value 30 in my_list: {index_of_30}")

# Print my_list
print(f"Final list: {my_list}")