fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("apple")
print(fruits)

removed_fruit = fruits.pop()
print(f"Removed fruit: {removed_fruit}")
print(fruits)

fruits.clear()
print(fruits)