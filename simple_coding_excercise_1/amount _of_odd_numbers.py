#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

i = 1
sum_of_odd = 0

#loop 10 times
while i <= 10:
    #ask user for a number
    number = int(input("Num "+str(i)+": "))
    #find if number is odd
    if number%2 == 1:
        #if number is odd add 1 to the sum
        sum_of_odd += 1
    i += 1

#print the sum of odd nums
print(sum_of_odd)
