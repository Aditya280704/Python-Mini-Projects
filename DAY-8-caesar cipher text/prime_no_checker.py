def prime_no(num):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False

    if is_prime == True:
        print("It is a prime number :")
    else:
         print("It is not a prime no:")
    
num = int(input("Enter a number :"))
prime_no(num)        
                