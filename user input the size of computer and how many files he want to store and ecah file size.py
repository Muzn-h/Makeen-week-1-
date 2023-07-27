#Program to let the user input the size of computer and how many files he want to store and ecah file size


x=float(input("Enter the computer size"))
n=int(input("Enter the number of files "))
y=float(input("Enter each file size"))

#It will go in progress in the if statment and them print out the result 
if (n*y<=x):
    print("Yes you can store")
else:
    print("Sorry you can't store")