person = {"name" : "Alice", "age" : 24, "grade": "A" }
print(person)

#Add new key-value pair
person["address"] = "123 abc"

#Update Age
person["age"] = 25

#Remove Grade
if "grade" in person:
    del person ["grade"]
print(person)