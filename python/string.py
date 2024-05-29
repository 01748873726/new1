str="hellow world"
print ("The original string  is : ",str)
reverse = "" 
count = len(str) 

while count > 0:   

    reverse += str[ count - 1 ]   

    count = count - 1  

print ("The reversed string using a while loop is : ",reverse)