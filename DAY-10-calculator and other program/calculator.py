# def add(a,b):
#     return a+b

# def subtract(c,d):
#     return c-d

# def multiply(e,f):
#     return e*f

# def divide(g,h):
#     return g/h

# random = int(input("Enter an operation to perform: 1.Addition 2.Subtraction 3.Multiplication 4.Division :"))
# num  = int(input("Enter first number to perform an operation :"))
# num1  = int(input("Enter second number to perform an operation :"))

# if random == 1:
#     result = add(num,num1)
#     print(f"Addition result is {result}")
# elif random == 3:
#     result = multiply(num,num1)
#     print(f"Multiplication result is {result}")
# elif random == 2:
#     result = subtract(num,num1)
#     print(f"Subtraction result is {result}")
# elif random == 4:
#     result =  divide(num,num1)   
#     print(f"Divison result is {result}")     


#Using dictionaries...
def add(a,b):
    return a+b

def subtract(c,d):
    return c-d

def multiply(e,f):
    return e*f

def divide(g,h):
    return g/h


operation = {"+":add, "-": subtract,"*":multiply,"/":divide}
# function = operation["+"]
# function(2,3)
def calculator():
    num  = float(input("Enter first number to perform an operation :"))

    for symbol in operation:
        print(symbol)
    should_continue = True    

    while should_continue: 
        operation_symbol = input("Pick an operation symbol from above : ")
        num1  = float(input("Enter second number to perform an operation :"))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num , num1)
        print(f"Result is {num} {operation_symbol} {num1} = {answer}")
        # if input(f"Type 'y' to continue calculating the {answer} or 'n' to exit and start a new calculation : ") == "y":
        #     num = answer
        # else:
        #     should_continue = False
        #     calculator()
        
        #this portion done by me adding an extra part for e to exit the code..
        option = input("Type 'y' to continue calculating, 'n' to start a new calculation, or 'e' to exit: ")
        if option == "y":
            num = answer
        elif option == "n":
            calculator()  # Start a new calculation
        elif option == "e":
            should_continue = False
            
calculator()
            #what if user wants to start a fresh calculation from line 49 then we use the concept of recursion:-
            #we create a function calculator and write the whole code inside it and call it within the function
            #here typing n exits the function if we write only else statement as false but now in new case we use recursion so we change it
        
            

    