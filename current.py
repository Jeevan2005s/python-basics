x=int(input("Enter the number of units:"))
if(x<100):
    y=x*0.5
    print("your bill is",y)
elif(x>100 and x<=200):
    y=x*1
    print("your bill is",y)
else:
    y=x*2
    print("your bill is",y)        