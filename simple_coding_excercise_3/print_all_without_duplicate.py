#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

duplicate = []
without_duplicate = []
inputs = []

for i in range(0,10,1):
    num = int(input("number " + str(i+1) + ": "))

    if num not in inputs:
        without_duplicate.append(num)
    elif num in inputs:
        duplicate.append(num)
        if num in duplicate and num in without_duplicate:
            without_duplicate.remove(num)

    inputs.append(num)
        
    

print(without_duplicate)
print(duplicate)
print(inputs)