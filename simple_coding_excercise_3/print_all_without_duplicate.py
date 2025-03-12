#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

#initialize lists
duplicate = []
without_duplicate = []
inputs = []

#loop 10 times
for i in range(0,10,1):
    num = int(input("number " + str(i+1) + ": "))

    #compare if in inputs
    if num not in inputs:
        without_duplicate.append(num)
    elif num in inputs:
        duplicate.append(num)
        #if the number is in duplicate it should not be seen in without a duplicate
        if num in duplicate and num in without_duplicate:
            without_duplicate.remove(num)

    inputs.append(num)
        
#show all without a duplicate   
print(without_duplicate)
