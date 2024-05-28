print("WEEKS LEFT CALCULATOR")

age = int(input("Enter your age:"))

# age = int(age)
 
a = (90-age)

a = int(a) #not necessary as a is already int in above statement 

b = (a * 52) # as 1 year has 52 weeks so we get total number of weeks inside b

print(f"you have {b} weeks left")#using f string

print("you have " +  str(b)   +  " weeks left")#using normal method