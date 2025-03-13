#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

inputs = []
all_nums = []
duplicates = []
most_duplicate = 0


while True:
    num = int(input("Enter a number: "))
    most_duplicate = num

    for numbers in range(len(inputs)):
        if num in inputs[numbers]:
            inputs[numbers].append(num)

        if len(inputs[numbers])>most_duplicate:
             most_duplicate = inputs[numbers][0]
    
    if num not in all_nums:
            inputs.append([num])

    all_nums.append(num)
    
    if num not in duplicates and num in all_nums:
        duplicates.append(num)




    print(inputs)
    print(all_nums)
    print(duplicates)
    print(most_duplicate)

