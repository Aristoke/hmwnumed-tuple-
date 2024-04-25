from collections import namedtuple

# Define a namedtuple for a Point with x and y coordinates
Point = namedtuple('Point', ['x', 'y'])

# Create a Point object
p1 = Point(1, 2)
print(p1.x, p1.y)  # Output: 1 2

p2 = Point(x=3, y=4)
print(p2.x)  # Output: 3
print(p2.y)  # Output: 4

data = (5, 6)
p3 = Point._make(data)
print(p3.x, p3.y)  # Output: 5 6

print(p1._asdict())  # Output: {'x': 1, 'y': 2}

p4 = p1._replace(x=10)
print(p4.x, p4.y)  # Output: 10 2

soz = input("so'z kiriting--> ")

print(soz[::-1])

p = 12345678

print(p[1:2:1])



