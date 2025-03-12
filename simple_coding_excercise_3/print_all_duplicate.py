#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

duplicate = []
inputs = []

for i in range(0,10,1):
    num = int(input("number " + str(i+1) + ": "))
    if num in inputs and num not in duplicate:
        duplicate.append(num)
    inputs.append(num)

print(duplicate)