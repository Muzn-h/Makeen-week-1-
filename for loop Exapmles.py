# for loop trying to list numbers from 1-5
for i in range (1,6):
    print(i , end =" " )
print(" ")
print(" ")

#print the for loop to print the shape 
n=6
for i in range (1,6):
    for i in range (1,n):
        print(i , end =" " )       
    print(" ")
    n -=1
    
print(" ")
    
#print tringle shape
n=1
for i in range (1,5):
    for i in range (n):
        print("*", end =" " )       
    print(" " )
    n+=1 
    
    
print(" ")
    
#print tringle shape
n=1
for i in range (1,6):
    for i in range (n):
        print("*", end =" " )       
    print(" " )
    n+=1
n=6
for i in range (0,6):
    for i in range (n):
        print("*", end =" " )       
    print(" " )
    n-=1