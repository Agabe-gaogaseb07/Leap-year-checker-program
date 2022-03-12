print("Welcome to the leap year checker")

input_year = int(input("Which year do you want to check?: "))

def is_leap(year):
    if (year%400 == 0) or (year%4==0 and year % 100 != 0):
        return True
    
    return False

if is_leap(input_year):
    print(f"{input_year} is a leap year")
    
else:
    print(f"{input_year} is not a leap year")
    