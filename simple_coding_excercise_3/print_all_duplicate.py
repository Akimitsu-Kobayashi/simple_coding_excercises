#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

#initialize lists
inputs = []

#loop 10 times
for i in range(0,10,1):
    #ask user for number
    num = int(input("number " + str(i+1) + ": "))
    #check if number is in the list
    if num not in inputs:
        inputs.append(num)

print(inputs)
