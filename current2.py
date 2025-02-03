x=int(input("Enter the value"))
if(x>200):
    x-=200
    print("your bill is",150+x*2)
elif(x>100):
    x-=100
    print("your bill is",50+x*1)
else:
    print("your bill is",x*0.5)     