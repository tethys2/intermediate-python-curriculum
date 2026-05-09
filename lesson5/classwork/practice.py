# Problem 1
# Create a class called Cat.
# It should have an __init__ that takes name.
# It should have a method called meow() that prints "<name> says meow!".
# Create a Cat and call meow().
class Cat:
    def __init__(self, name):
        self.name = name
    
    def meow(self):
        print(self.name, "says meow!")
    
cat = Cat("Mochi")
cat.meow()


# Problem 2
# Create a class called Rectangle.
# __init__ should take width and height.
# Make a method area() that returns width * height.
# Create a Rectangle and print its area.

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
r = Rectangle(5, 3)
print("Area:", r.area())


# Problem 3
# Create a class called Counter.
# It starts at value 0.
# Make a method add_one() that increases the value by 1.
# Call add_one() 5 times and print the final value.

class Counter:
    def __init__(self):
        self.value = 0

    def add_one(self):
        self.value = self.value + 1

c = Counter()
for i in range(5):
    c.add_one()
print("Final value:", c.value)


# Problem 4
# Create a class called Player.
# __init__ takes name and health.
# Make a method take_damage(amount) that subtracts from health (no negatives).
# Create a Player and test take_damage().

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health = self.health - amount
        if self.health < 0:
            self.health = 0

p = Player("Aarav", 10)
p.take_damage(6)
print(p.name, "health:", p.health)
p.take_damage(20)
print(p.name, "health:", p.health)


# Problem 5
# Create a class called Book.
# __init__ takes title and pages.
# Make a method is_long() that prints "Long" if pages >= 300, else prints "Short".

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        
    def is_long(self):
        if self.pages >= 300:
            print("Long")
        else:
            print("Short")

b = Book("Harry Potter", 500)
b.is_long()