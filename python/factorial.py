num=int(input("enter a num:"))
ans=1
if num<0:
    print("no factorial")
elif num ==0:
    print("the factorial of 0 is 1") 
else:
    for i in range(1,num+1):
        ans=ans*i 
print("the factorial of ",num,"is",ans)              
