print("Welcome to the leap year checker")
#Here the year needs to be stored as a integer value to give the same output.
input_year = int(input("Which year do you want to check?: "))

#Assigning the is_leap(year), can help me calculate the if the year is divisible by 400 and 4 and not 100. If true then its a leap year, and if not then not a leap year.
def is_leap(year):
    if (year%400 == 0) or (year%4==0 and year % 100 != 0):
        return True
#!!    
    return False

#Then give it an if statement which will then check if the year is divisible by meaning the above mentioned numbers.
if is_leap(input_year):
    print(f"{input_year} is a leap year")
#Then print if assigned duty to tell if it's a leap year, and or (else) meaning if it is not a leap year and will print that with the print statement below the (else:) call function.    
else:
    print(f"{input_year} is not a leap year")
    
