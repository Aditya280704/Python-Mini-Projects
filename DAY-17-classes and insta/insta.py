class User:
    def __init__(self,userid,username):
        self.id = userid
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self,user):
        #user to know the user we followed..
        #self cz when this method is called it knows the object that called it...
        user.followers +=1
        self.following +=1
user_1 = User("001","Angela")
user_2 = User("002","Jack")    

user_1.follow(user_2)    
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)