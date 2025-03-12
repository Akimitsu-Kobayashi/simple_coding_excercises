#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

#ask user to input 2 numbers
num_1 = int(input("number 1: "))
num_2 = int(input("number 2: "))

#find the lower number to use as the starting range
if num_1 < num_2:
    #loop based on the range of the 2 numbers   
    for number in range(num_1+1,num_2,1):
        print(number)
else:
    #loop based on the range of the 2 numbers
    for number in range(num_2+1,num_1,1):
        print(number)

