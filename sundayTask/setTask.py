from functionsForThisTask import *

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
print(union_set)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")


# to remove a set
set1 = {1, 2, 3, 4, 5}
set1.clear()

# minimum and maximum
max_value = maxOf(set2)
min_value = minOf(set2)

# length of my set
print(lengthOf(set2))



