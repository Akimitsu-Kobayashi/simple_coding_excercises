#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

inputs = []

#loop forever
while True:
    #tries untill there is an error
    try:
        #asks user for a number
        num = int(input("Enter a number: "))
        inputs.append(num)

        #finds then max value in the list
        highest_num = max(inputs)

        print("highest number is "+ str(highest_num))

    except ValueError:
        #error when the input is wrong
        print("Invalid input")
        break