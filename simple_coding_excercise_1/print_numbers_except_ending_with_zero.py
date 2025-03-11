#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

#loop 100 times
for number in range(1,101,1):

    #if doesnt number ends with 0 print the number
    if number%10 != 0:
        print(number)