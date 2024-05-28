import random

random_number = random.randint(1,20)

print(random_number)


random_float = random.random()#gives random float number between 0 to 1...
random_float * 5 #this will give us value beyond 1... check the function on pycharm..
print(random_float)

# Heads or Tails 
random_side = random.randint(0,1)

if random_side == 0:
    print("Heads")
    
else:
    print("Tails")    


love_score = random.randint(1,100)
print(f"Your love score is {love_score}")



