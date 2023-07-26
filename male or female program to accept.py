#INPUT THE GENDER 
Gender=input ("Enter your gender Female or Male")

'''THE IF NESTED STATETMENT CHECK THE GENDER AND IF IT'S MALE WILL DIRECTLY RETURN REJECTED.
OTHERWISE WILL AKS ABOUT THE AGE IF ITS ABOVE OR EUQL 24 AND 30 WILL RETURN ACCEPTED
IF THE AGE NOT IN THE RANG ITS RETURN REJECED'''
if(Gender=="Female"):
    Age=int(input("Enter your Age:"))
    if (24<=Age<30):
        print("You are Accepted")
else:
    print("You are Rejected")
      
        
 