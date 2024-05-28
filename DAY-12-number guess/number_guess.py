import random

guess = random.randint(1,100)
level = input("Choose which level you want to play : Enter e for Easy and h for Hard : ")
def easy():
        chance = 10
        print("You Have 10 chances , start guessing the number")
        while chance > 0:
            
            player_guess = int(input("Enter a number : "))
            if player_guess == guess:
                print("You got the correct guess ")
                return
            elif player_guess < guess:
                print("Too low")
                chance -= 1
                print(f"you have {chance} remaining ")
            elif player_guess > guess:
                print("Too high")
                chance -= 1  
                print(f"you have {chance}remaining ")
            if chance == 0:
                exit()            
def hard():          
        chance = 5
        print("You Have 5 chances , start guessing the number")
        while chance > 0:
            
            player_guess1  = int(input("Enter a number: "))
            if player_guess1 == guess:
                print("You got the correct guess ")
            elif player_guess1 < guess:
                print("Too low")
                chance -= 1
                print(f"you have {chance} remaining ")
            elif player_guess1 > guess:
                print("Too high")
                chance -= 1   
                print(f"you have {chance} remaining ") 
            if chance == 0:
                exit()      
if level == 'e':
    easy()
if level == 'h':
    hard()
             
#CHATGPT:-            
# import random

# guess = random.randint(1, 100)

# level = input("Choose which level you want to play: Enter 'e' for Easy and 'h' for Hard ")

# def easy():
#     if level == "e":
#         chance = 10
#         while chance > 0:
#             player_guess = int(input("Enter a number: "))
#             print("You have", chance, "chances left. Start guessing the number.")
#             if player_guess == guess:
#                 print("You got the correct guess!")
#                 return
#             elif player_guess < guess:
#                 print("Too low")
#             elif player_guess > guess:
#                 print("Too high")
#             chance -= 1
#         print("You have run out of chances. The correct number was:", guess)
#         exit()

# def hard():
#     if level == "h":
#         chance = 5
#         while chance > 0:
#             player_guess = int(input("Enter a number: "))
#             print("You have", chance, "chances left. Start guessing the number.")
#             if player_guess == guess:
#                 print("You got the correct guess!")
#                 return
#             elif player_guess < guess:
#                 print("Too low")
#             elif player_guess > guess:
#                 print("Too high")
#             chance -= 1
#         print("You have run out of chances. The correct number was:", guess)
#         exit()

# if level == "e":
#     easy()
# elif level == "h":
#     hard()
# else:
#     print("Invalid level choice. Please enter 'e' for Easy or 'h' for Hard.")
             