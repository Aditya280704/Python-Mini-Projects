class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale,Exhale")
        
        
class Fish(Animal):
    def __init__(self):
        super().__init__() 
        
    def breathe(self):
         super().breathe() #but we want to modify and add one line   
         print("Doing this underwater")
    def swim(self):
        print("Moving in Water") 
        
        
nemo = Fish()
nemo.swim()
nemo.breathe()  #method inherited from animal class and used in fish class...                    