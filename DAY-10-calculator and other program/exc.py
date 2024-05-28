# year = int(input("enter a year: "))
# if(year % 4 == 0):
#     print("It is a Leap Year ")
# elif(year % 100 == 0 and year % 400 == 0):
#     print("Leap year ")
# else:
#     print("Not a Leap Year ")        



# def leap_year(year):
#     if(year % 4 == 0):
#         print("It is a Leap Year ")
#     elif(year % 100 == 0 and year % 400 == 0):
#         print("Leap year ")
#     else:
#         print("Not a Leap Year ")        
# leap_year(int(input("Enter a Year : ")))        

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False



#year % 4 = 0 so leap year , year % 100 = 0 may or may not be leap year
#year % 400 = 0 so leap year 
#If the condition year % 400 == 0 is False, it means the year is divisible by 100 but not by 400, so it's not 
# a leap year. 
# The function returns False in this case



def days__in_month(year , month):
    month_day = [31 , 28 , 31 , 30 , 31 , 30 , 31, 31 ,30 ,31 ,30 ,31]
    if month == 2 and leap_year(year):
        # print("29")
        return 29
    else:
        return month_day[month - 1]
    if month == 1:
        return 31
    if month == 3:
        return 31
    if month == 4:
        return 30
    if month == 5:
        return 31
    if month == 6:  
        return 30      
    if month == 7:
        return 31
    if month == 8:
        return 31 
    if month == 9:
        return 30
    if month == 10:
        return 31
    if month == 11:
        return 30
    if month == 12:
        return 31    
                


a = int(input("Enter a Year: "))
b = int(input("Enter a Month: "))
print(days__in_month(a,b))