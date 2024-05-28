print("Hello"[4]) #to print single letter O this method is called subscripting and we can print any letter..

# a=len(input("Enter your name:"))
# print("your name has " + a + " charecters")
#error as we are concatinating string to int as we have written len function which returns an integer value..

a=len(input("Enter your name:"))
print(type (a))
#change the type of a from int to string
b=str(a)
print("your name has " + b + " charecters")

#converting the string to float data type and then adding it to integer data type..
print(70  + float("100.5"))



#Mathematical operators:-
2+3 #addition
3-2 #subtraction
2*3 #multiplication
6/3 #division
#to raise to power here 2 to the power 3..
print(2**3) 


#priority order
# ()
# **
# * /
# + -
print(3*3+3/3-3)


#rounding number
print(8/3)
print(round(8/3))
print(round(8/3,2))# ,2 shows to round to 2 decimal places
print(8//3)
print(type(8//3))