#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

#loop 10 times
i = 0
sum_of_numbers = 0
first_number = 0

while i < 10:
    #ask user for a number
    num = int(input("number " + str(i + 1) + ": "))
    
    #store first number
    if i == 0:
        first_number = num
    else:
        sum_of_numbers += num
    
    i += 1

#print first number minus the sum
print(first_number - sum_of_numbers)