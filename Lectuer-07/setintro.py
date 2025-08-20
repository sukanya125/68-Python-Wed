setA = {1,2,3,4}
setB = set([8,9,10])

setA.add(5)  # Adding an element to setA
setB.update([6,7])
Uset = setA | setB  # Union of setA and setB
print(Uset)
print(len(Uset))  # Length of the union set

setB.update('ABCD')
setA.update(['6,7,8'])  # Adding characters to sets
print(setB)

print(setA.intersection(setB))  # Intersection of setA and setB
print(setA ^ setB)  # Check if setA is a subset of setB

setB.remove('B')  # Removing an element from setB
setB.discard('10')  # Discarding an element from setB
print(setB)
print(setA.clear())  # Clearing setA
for val in Uset:
    print(val)  # Iterating through the union set