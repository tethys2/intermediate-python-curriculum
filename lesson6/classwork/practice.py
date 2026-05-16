# Problem 1
# Create a tuple called colors with 3 colors.
# Print the first color and the last color.
colors = ("red", "green", "blue")
print(colors[0])
print(colors[-1])

# Problem 2
# Create a tuple called location with (city, state).
# Unpack it into city and state variables and print them.

location = ("Seattle", "WA")
city, state = location
print(city)
print(state)

# Problem 3
# Create a list of tuples called points with 3 points:
# (0, 0), (2, 5), (4, 1)
# Loop through points and print each x and y.

points = [(0,0), (2, 5), (4,1)]
for p in points:
    x, y = p
    print("x:", x, "y:", y)

# Problem 4
# Ask the user for two numbers.
# Store them in a tuple and print the tuple.

a = int(input("Enter a number: "))
b = int(input("Enter another number"))
pair = (a,b)
print(pair)


# Problem 5
# Create a function called add_and_multiply(a, b).
# It should return (a + b, a * b) as a tuple.
# Call it and unpack the results, then print both.

def add_and_multiply(a,b):
    return a + b, a * b

s, p = add_and_multiply(3,4)
print("Sum:", s)
print("Product:", p)

