# fruits = ['mango','apple','banana']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + ' pie')
    
heights = [123,156,345,213,222,143]

total_height = 0

for height in heights:
    total_height += height

average_height = total_height / len(heights)

print(f"Average height is {average_height}")         



#for loop using range

for number in range(1,11):
    print(number)
    
    
#for skipping number in a given range here skipping 3 numbers..

for number in range(1, 11 , 3):
    print(number)
        

#for adding number till 100
total = 0
for number in range(1,101):
    total+=number
print(total)        


#code for adding sum of all even numbers
total = 0
for number in range(0,11,2):
    total +=number
print(total)    
    
    