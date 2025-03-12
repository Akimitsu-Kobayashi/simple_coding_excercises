#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

#ask user for 2 numbers
num_1 = float(input("number 1: "))
num_2 = float(input("number 2: "))

#divide 2 numbers 
quotient = round(num_1/num_2)

#print quotient rounded up to the nearest whole number
print(quotient)
