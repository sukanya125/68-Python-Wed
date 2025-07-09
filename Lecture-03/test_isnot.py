a = [1 , 2, 3]
b = a

c= [1, 2, 3]
d= [1, 2, 3]

print(a is b)  # True, same object
print(a is c)  # False, same object
print(c is d)  # False, different objects with same content

print(a == b)  # True, same content
print(a == c)  # True, same content