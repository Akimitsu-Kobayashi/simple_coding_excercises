#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

inputs = []
all_nums = []
duplicates = []

while True:
    num = int(input("Enter a number: "))

    for i in range(len(inputs)):
        if num in inputs[i]:
            inputs[i].append(num)
    
    if num not in all_nums:
            inputs.append([num])

    if num not in duplicates and num in all_nums:
        duplicates.append(num)

    all_nums.append(num)



    
    print(inputs)
    print(all_nums)
    print(duplicates)

