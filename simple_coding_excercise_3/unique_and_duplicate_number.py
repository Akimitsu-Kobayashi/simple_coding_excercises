#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

#initialized list
inputs = []

#loop forever
while True:
    #tries untill there is an error
    try:
        #asks user for a number
        num = int(input("Enter a number: "))

        #prints unique if in list and duplicate when not on list
        if num not in inputs:
            print("Unique")
        elif num in inputs:
            print("Duplicate")
        #adds number to the list
        inputs.append(num)

    except ValueError:
        #error when the input is wrong
        print("Invalid input")
        break