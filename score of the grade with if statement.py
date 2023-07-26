#PROGRM TO GETTING THE SCORE OF THE GRADE
#FIRST INPUT TTHE GRADE 
Grade= float(input("Enter your grade:"))

#IF STATMENT TO CHECK THE GRADE IN WHICH SCALE TO PRINT OUT THE SCORE OF IT 
if (Grade>90):
    print("A")
elif (80<Grade<=90):
    print("B")
elif (60<=Grade<=80):
    print("C")
elif (60<Grade):
    print("D")
else:
    print("Failed")