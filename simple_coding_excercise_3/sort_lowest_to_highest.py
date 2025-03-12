#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

inputs = []

#loop forever
while True:
    #tries untill there is an error
    try:
        #asks user for a number
        num = int(input("Enter a number: "))
        inputs.append(num)

        #finds then minimum value in the list
        sorted_inputs = sorted(inputs)

        print(sorted_inputs)

    except ValueError:
        #error when the input is wrong
        print("Invalid input")
        break