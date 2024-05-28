import math
def paint(height,width,cover):
    num = (height * width)/cover
    round_up = math.ceil(num)#round up to smallest integer closest to decimal figure
    print(f"You'll need {round_up} cans of paint")

height= int(input('Enter the height:'))
width=int(input("Enter the width:"))
cover = int(input("enter the coverage area:"))
paint(height,width,cover)    
    