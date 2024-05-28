import random

a = int(input("Enter 1 for Rock , 2 for Paper , 3 for Scissor: "))

random_choice = random.randint(1,3)

if a == 1 and random_choice == 1:
    print("Tie")
elif a==1 and random_choice == 2:
    print("you loose")
elif a==1 and random_choice == 3:
    print("you win")
elif a==2 and random_choice == 1:
    print("you win")
elif a==2 and random_choice ==2:
    print("tie")
elif a==2 and random_choice==3:
    print("you loose")
elif a==3 and random_choice==1:
    print("you loose")
elif a==3 and random_choice==2:
    print("you win")
elif a==3 and random_choice==3:
    print("tie")               
    

                