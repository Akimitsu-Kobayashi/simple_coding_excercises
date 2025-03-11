#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

#get 2 numbers from user and covert to float
num_1 = float(input("number 1: "))
num_2 = float(input("number 2: "))

#divide the 2 numbers
quotient = round(num_1/num_2,2)

#print the quotient
print(quotient)