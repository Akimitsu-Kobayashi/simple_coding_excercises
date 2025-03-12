#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

#loop until 100
number = 0
while number < 101:
    #find if number is ending with 0 or 5
    if number%5 != 0:
        #print number
        print(number)
    number += 1

# if not print the number