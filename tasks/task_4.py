"""
Task 4: Dictionaries, aka `dict`

- are you familiar and confident with: `strings` and `ints`
- are you familiar and confident with: `lists` and `dictionaries`
- are you familiar and confident with: `functions`

=======
Brief:

See if you can build a dictionary of 5 people, with their ages, best time in mario kart and height.

Then, print the:
- tallest,
- oldest and/or
- person with fastest time

"""

# SOME TYPES

am_i_cool = True
# print(am_i_cool)

if am_i_cool == "TRUE":
    print("I am cool cos it's equal equal")
elif am_i_cool:
    print("I am cool")
else:
    print("You ain't cool!")

name = "Kai"  # string
age = "41"  # actually string
age2 = 41  # float
age3 = 41.5  # float

# print(age3 * 2)

# to protect against python 2 wanting to round down an int
# print(age2 / 2.0)

# LISTS

names = ["Daniel", "Saif", "Kai"]

# print(len(names))
# print(sorted(names, reverse=True))

names.append("Chiwoon")

# print(len(names))
# print(sorted(names, reverse=True))

# DICTIONARY

people = {}
people["Kai"] = {"is_cool": True}
people["Saif"] = {"is_cool": True}

# print(len(people))

# print(sorted(names)[-1])
print("Saif", "is cool?", people.get("Saif").get("is_cool"))

# people["Kai"] = 25
# people["Saif"] = 26
# people["Daniel"] = 126

# print(people)

for p in people:
    # print(p, people[p].get("is_cool"))
    print(p, people[p].get("is_this_person_cool"))
    # print(p, people[p]["is_this_person_cool"])
