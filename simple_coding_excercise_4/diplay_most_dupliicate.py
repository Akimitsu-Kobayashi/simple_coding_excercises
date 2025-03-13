#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

inputs = []
all_nums = []
duplicates = []
most_duplicate = 0
most_duplicate_counter = 0
i = 1

while i>0:
    num = int(input("Enter a number: "))
    if i == 1:
        most_duplicate = num
    
    for numbers in range(len(inputs)):
        if num == inputs[numbers][0]:
            inputs[numbers].append(num)

        if len(inputs[numbers])>len(duplicates):
             duplicates = inputs[numbers]
             most_duplicate = inputs[numbers][0]
             
    if num not in all_nums:
            inputs.append([num])

    all_nums.append(num)
    i += 1

    print(most_duplicate)
    print(duplicates)
    print(inputs)




