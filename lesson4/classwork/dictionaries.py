person = {
    "name" : "Alex",
    "age" : 15,
    "city" : "Seattle"
}

print(person)
print("Name:", person["name"])
print("Age:", person["age"])

person["favorite_food"] = "Pizza"
print(person)

person["age"] = person["age"] + 1
print("New age:", person["age"])

print("name" in person)
print("height" in person)