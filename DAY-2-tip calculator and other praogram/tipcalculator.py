print("WELCOME TO TIP CALCULATOR")
amount = input("Enter the total amount of bill: ")

amount = float(amount)

tip = input("Enter the percentage of tip you want to add to bill: ")

tip = float(tip)

a = (amount + tip/100)

c = input("Enter the number of persons the bill is splitting amongst:")

c = float(c)

b = (a/c)

print(f"Each person has to pay {b} bucks ")


