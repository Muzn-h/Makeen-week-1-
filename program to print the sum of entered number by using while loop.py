# program to print the sum of entered number by using while loop 
n = int(input("enter a number"))
total = 0
while (n>0):
    digit = n % 10
    total += digit
    n = n//10
print (total)
    
    
