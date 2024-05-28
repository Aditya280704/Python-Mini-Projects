def greet():
    print("Hello Aditya")
    print("Good morning!")
    print("Ain't the weather nice?")

greet()    

#function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"how do you do {name}")
greet_with_name("Angela")    

#function taking 2 parameters
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")
greet_with("Aditya","Goa") 
greet_with("Goa","Aditya") #first argument gets assigned to first parameter
#and second one with 2nd argument 
#this is called positional argument in python..

#KEYWORD ARGUMENTS:
greet_with(name = "aditya" , location = "london")
greet_with(location = "london",name = "aditya")
   