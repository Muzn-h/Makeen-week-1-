#Making a program for a calcolator to do some calculated operation
#Firstly ask the user to input float numbers and the operation that want to do it 
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
opr = input("Enter operation:")

#How each operation does it go to work and print the result out 
if (opr=="+"):
    print(num1+num2)
elif (opr=="-"):
    print(num1-num2)
elif (opr=="*"):
    print(num1*num2)
elif (opr=="/"):
    print(num1/num2)
#if the user input any operation not mentioned above it return INVALID
else:
    print("Invalid Operation")




