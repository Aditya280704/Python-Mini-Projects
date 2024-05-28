print("Welcome to the rollercoaster: ")
height = int(input("Enter your height in cms "))
print(type(height))
bill = 0


if height >= 120:
    print("You can ride on rollercoaster")
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
        print("child tickets are $5")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    photo = input("do you want a photograph yes / no ?")
    if photo == "yes":
        bill = bill + 3
        print(f"Final amount is ${bill}")
                
else:
    print("goodbye!!")    