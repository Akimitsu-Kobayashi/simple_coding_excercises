#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#initialize lists
duplicate = []
inputs = []

#loop 10 times
for i in range(0,10,1):
    #ask user for number
    num = int(input("number " + str(i+1) + ": "))

    # if the number is in inputs and not in dplicate list (so that there wouldnt be repetition of duplicate in list) 
    if num in inputs and num not in duplicate:
        #then add the num to the duplicate list
        duplicate.append(num)
    inputs.append(num)

print(duplicate)