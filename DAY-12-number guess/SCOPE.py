#LOCAL SCOPE

def drink_potion():
    potion_strength  = 2
    print(potion_strength)

drink_potion()   
# print(potion_strength) #shows error because potion strength 
#can only be accessed inside the function and not outside 
#eg of apple tree inside house fence

#GLOBAL SCOPE:
player_health = 10
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    player_health = 12
    print(player_health)

drink_potion()    
#here player health can be accessed inside as well as outside the function
#as it is predefined outside the function and so it is called global scope



#if we nest this function innside other function then also we cannot see for eg here
#we cannot access drink potion outside the game function we have to keep it in walls of drink portion function..

def game():
    def drink_potion():
        potion_strength  = 2
        print(potion_strength)

    drink_potion()   
    
#THERE IS NO BLOCK SCOPE IN PYTHON..    

game_level = 3
enemies = ["skeleton","zombie","alien"]
if game_level < 5:
    new_enemies = enemies[0]
print(new_enemies)    
#we do not get error even if we print new enemies outside the function because there
#is no BLOCK SCOPE (i.e in function like if ,while etc.. )but as soon as we create a fuction
#then we cannot print the same statment outside the function as it will show an error..
game_level = 3
def create_enemy():
    enemies = ["skeleton","zombie","alien"]
    if game_level < 5:
        new_enemy = enemies[0]
# print(new_enemy)    #shows error


#MODIFYING GLOBAL SCOPE
enemies = 1
def increase_enemies():
    global enemies #if we do not write this line then enemies+=1 shows error because we have to write either this
    #or enemies = 1 both are same..because these lines tell us that in next line we increase their value by 1.
    enemies += 1
    print(f"enemies inside function {enemies}")

increase_enemies()  
print(f"enemies outside function {enemies}")  

#GLOBAL CONSTANT 
PI = 3.14159
#made with caps so that we never change them again in future 
URL = "www.google.com"


