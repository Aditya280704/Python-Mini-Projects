name1 = input("Enter Your Name: ")
name2 = input("Enter Other persons name:")
combined = name1 + name2
print(type(combined))
lowername = combined.lower()

t = combined.count("t")
r = combined.count("r")
u = combined.count("u")
e = combined.count("e")

firstdigit = t+r+u+e

l = combined.count("l")
print(type(l))
o = combined.count("o")
v = combined.count("v")
e = combined.count("e")

seconddigit = l+o+v+e
print(type(seconddigit))

score  =str(firstdigit)+str(seconddigit) #str used so as to concatinate both the digits
print("your score is:",score)