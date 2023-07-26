#clock syatem
##enter the hour in 24 hour system and the min spreatly for each hour 
Hour1=int(input("input the first hour in 24 h"))
Min1=float(input("input the minutes in first hour"))

Hour2=int(input("input the second hour in 24 h"))
Min2=float(input("input the minutes in scond hour"))

''' the program will check the first hours if one of them is bigger so it come first .whereas, if there are equal
it will check the min of each hour and then will print out the result '''
if (Hour1<Hour2):
           
    print(Hour1,"is come the first")

else:
    if(Hour1==Hour2):
           if(Min1<=Min2):
               print(Hour1,"is come first")
           else:
               print(Hour2,"is come first")
    else:
        print(Hour2,"is come first")
           
           
           
        

