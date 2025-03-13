#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

#initialize lists and variables
inputs = []
all_nums = []
duplicates = []
most_duplicate = 0
i = 1

while i>0:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
         print("Invalid Input")
         break
    # the first inputs sets most duplicate first input
    if i == 1:
        most_duplicate = num
    
    #loops on each nested list inside the list if the number is in the nested list
    for numbers in range(len(inputs)):
        if num == inputs[numbers][0]:
            #appends num when it is equal to the nested list e.g.(num = 3 and the list is = [3,3,3] so it will be appended to that nested list)
            inputs[numbers].append(num)

        #finds the nested list with the most length and sets it as the most duplicate in the list
        if len(inputs[numbers])>len(duplicates):
             duplicates = inputs[numbers]
             most_duplicate = inputs[numbers][0]
             
    if num not in all_nums:
            inputs.append([num])

    all_nums.append(num)
    i += 1

    print(most_duplicate)

    #essentially the program sorts the number to separate nested loops and finds the length of those nested loop to compare what is bigger




