height = float(input("Height in meters:  "))
weight = int(input("Weight in kgs:  "))

if height > 3:
    raise ValueError("The human height should not be over 3 metres ")

bmi = weight/height**2
print(bmi)
