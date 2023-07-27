# program to convert decrypte a message
message=input("enter the encrypted message")

for i in message:
    ascii = int(ord(i)-3)
    print (chr(ascii),end="")
    



    
    


