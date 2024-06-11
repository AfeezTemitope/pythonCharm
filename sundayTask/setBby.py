def sum_collection(collection):
    return sum(collection)

def remove_item(collection, item):
    if item in collection:
        collection.remove(item)
        return item
    else:
        return None

def find_intersection(set1, set2):
    return set1.intersection(set2)

numbers = set()
while len(numbers) < 10:
    num = int(input("Enter a number: "))
    numbers.add(num)

print("Collection:", numbers)

print("Sum of collection:", sum_collection(numbers))

removed_item = remove_item(numbers, 5)
if removed_item is not None:
    print("Removed item:", removed_item)
else:
    print("Item not found in collection")

set2 = {1, 2, 3, 4, 5}
print("Intersection:", find_intersection(numbers, set2))