total = 0
for number in range(1,11):
    total = total + 1
    if total % 3 == 0:
        print(total)
        print("Fizz")
    elif total % 5 == 0:
        print(total)
        print("Buzz")
    elif total % 3 and total % 5 == 0:
        print(total)
        print("FizzBuzz")
                