#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

inputs = []

while True:
    try:
        num = int(input("Enter a number: "))

        if num not in inputs:
            print("Unique")
        elif num in inputs:
            print("Duplicate")

        inputs.append(num)

    except ValueError:
        print("Invalid input")
        break