dictionary = {"Bug":"error in program", "Function":"piece of code u can call over again and again"}
#bug = key and definition is the value..
print(dictionary["Bug"])

#adding new items to dictionaries
dictionary["Loop"] = "Action of doing something again and again"
# print(dictionary)

#empty dictionary
empty_dictionary = {}

#wipe and entire dictionary
dictionary = {}
# print(dictionary)

#edit an item in dictionary
dictionary["Bug"] = "a moth in your computer"
# print(dictionary)

#loop through dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])