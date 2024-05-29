string=input("enter a string")
reverse_srting=""
index=len(string)-1
while index>=0:
    reverse_srting+=string[index]
    index-=1
print("reverse_string",reverse_srting)    
