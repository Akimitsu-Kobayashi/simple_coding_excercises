#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

#loop 10 times
i = 0
sum_of_ten_num = 0
while i < 10:
    #ask user for a number
    input_num = int(input("number"+ str(i+1) +":"))
    #add number to the sum of all numbers
    sum_of_ten_num += input_num
    i += 1

#print the sum
print(sum_of_ten_num)