#nested if
state=input("enter your graduation state 'yes or no'")
age=int(input("enter your age :"))

if (age>=18):
    
    if (state=="yes"):
        print("Graduate and the age is ", age ,"years old ")
    else:
        print("Not Graduated and the age", age , "years old")
else:
    print("the age is undr 18 years old")