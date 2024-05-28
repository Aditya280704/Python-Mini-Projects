#create your own class
class User:
    #pass #if we do not want anything we write pass so that program does not show 
#indent error..(error when we do not write anything inside class or function and just keep it empty)
    def __init__(self):
        #used to initialize attributes 
       print("New User being created")
       #everytime a new user is created eg below this print statment will get triggered  
    
        
    
user_1 = User()   
#how to create attribute for that class
user_1.id = "001"
user_1.username = "Aditya"
print(user_1.id)

user_2 = User()
user_2.id = "002"
user_2.username = "Anil"
print(user_2.id)
  
  
  
# OTHER WAY:-  
class User:
    def __init__(self,userid,username):
        self.id = userid
        self.username = username
user_1 = User("001","Aditya")
print(user_1.username)
user_2 = User("002","Anshul") 
print(user_2.username)       