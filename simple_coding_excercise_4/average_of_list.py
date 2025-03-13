#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

inputs = []

#loop forever
while True:
    #tries untill there is an error
    try:
        #asks user for a number
        num = int(input("Enter a number: "))
        inputs.append(num)

        #average of list
        average_of_list = sum(inputs) / len(inputs)
        

        print(average_of_list)

    except ValueError:
        #error when the input is wrong
        print("Invalid input")
        break