from math import *
PI=22/7 # IMPORT THE PI VALUE

L=int (input( "please enter Length=")) # ASK THE USER INPUT THE LENGTH OF THE SHAPE  
H=int (input( "please enter height=")) # ASK THE USER TO INPUT THE HEIGHT OF THE SHAPE

#APPLY THE AREA RULES OF EACH  OF  
Area1 = (4*L) # THE RULE OF SQUARE'S AREA
Area2  = (L/2*H) # THE RULE NEEDED FOR TRIANGLE AREA
Area3 = (PI * (L/2) ** 2) # THE RULE OF CIRCLE AREA 

#THE EQUATION NEEDED TO CALCULATE THE TOTAL AREA OF THE SHAPE BY GEETING THE TOTAL AREA OF SUQARE ADDED TO TRIANGLE AREA SUBTRACTING FROM TOTAL CIRCLE AREA 
sum= (Area1 + Area2 )-Area3

#TO GTTING TH RESULT WE NEED TO PRINT OUT THE SUM
print(sum)

