#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

inputs = []
lowest_number = 0

#loop forever
while True:
    #tries untill there is an error
    try:
        #asks user for a number
        num = int(input("Enter a number: "))

        for number in inputs:
            if number < num:
                lowest_number = number
            else:
                lowest_number = num
        print(lowest_number)
        inputs.append(num)

    except ValueError:
        #error when the input is wrong
        print("Invalid input")
        break