point = (8, 2)
x, y = point

print("x:", x)
print("y:", y)

a = 5
b = 9

a, b = b, a
print(a, b)

def min_and_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest

nums = [4, 12, 7, 1, 9]
mn, mx = min_and_max(nums)
print("Min:", mn)
print("Max:", mx)