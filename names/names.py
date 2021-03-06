import time

from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# duplicates = set(names_1).intersection(names_2)
# return_value = [x for x in duplicates]

bst_1 = BSTNode(names_1[0])

for name_1 in names_1[1:]:
    bst_1.insert(name_1)


bst_2 = BSTNode(names_1[0])

for name_2 in names_2[1:]:
    bst_2.insert(name_2)


def add_to_list(value):
    for name_2 in names_2:
        if value == name_2:
            duplicates.append(name_2)

bst_1.for_each(add_to_list)
        



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
