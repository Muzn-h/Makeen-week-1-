#program to calculate the bill of the user by inputig the unit 
Unit= float(input("Enter your electricity bill:"))

#by if and else if statement we check the conditions to print the result 
if (Unit<100):
    print("No Charge")
elif (200>Unit>100):
    Unit*=0.024
    print("Your bill is",Unit)

elif (Unit>200):
    Unit*=0.047
    print ("Your bill is",Unit)
