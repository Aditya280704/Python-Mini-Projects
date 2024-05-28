import random

names = ["Aditya","Ayush","Aryan","Dhruv"]

len(names)
print(len(names))

random_choice = random.randint(0,len(names)-1)
person_paying = names[random_choice]

print(f"Person paying is {person_paying}")