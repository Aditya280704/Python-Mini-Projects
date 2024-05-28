#use of list , for loops , randomization etc...
import random

alphabets = ["a","b","c","d","e","f","g"]
numeric = ["1","2","3","4","5","6","7","8","9","10","11"]

passalph = int(input("Enter how many alphabets u want in password:"))
passnum = int(input("Enter how many numeric u want in ur password:"))

password = ""
for alphabet in range(1,passalph+1):
    random_choice = random.choice(alphabets)
    password = password + random_choice
print(password)#do not keep this in the loop as it will print the password like
#d
#de
#deb
      
pass1 = ""
for numerics in range(1,passnum+1):
    random_numeric = random.choice(numeric)
    pass1 = pass1 + random_numeric
print(pass1)

final_password = password + pass1   
print(f"password is {final_password}")



#CHATGPT CODE:-    
    
# import random

# alphabets = ["a", "b", "c", "d", "e", "f", "g"]
# numeric = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

# passalph = int(input("Enter how many alphabets you want in password: "))
# passnum = int(input("Enter how many numeric characters you want in your password: "))

# password = ""
# for _ in range(passalph):
#     random_choice = random.choice(alphabets)
#     password += random_choice

# print("Alphabets in password:", password)

# pass1 = ""
# for _ in range(passnum):
#     random_numeric = random.choice(numeric)
#     pass1 += random_numeric

# print("Numerics in password:", pass1)

# final_password = password + pass1   
# print(f"Password is: {final_password}")
    
       