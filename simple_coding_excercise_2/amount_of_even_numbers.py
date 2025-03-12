#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

#loop 10 times
i = 0
even_numbers = 0

while i < 10:
    #ask user to input a number
    num = int(input("number" + str(i + 1) + ": "))
    
    #check if the number is even
    if num % 2 == 0:
        even_numbers += 1
    
    i += 1   
#print the count

print(even_numbers)