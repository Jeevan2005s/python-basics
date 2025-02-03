x=int(input("Enter the amount:"))
if(x>=500):
    y=x*0.2
    x-=y
    print("You got 20% discount,your discounted price",x)
elif(x>=250):
    y=x*0.1
    x-=y
    print("You got 20% discount,your discounted price",x)
elif(x>=100):
    y=x*0.05
    x-=y
    print("You got 5% of discount,your discounted price is",x)    
else:
    print("Your bill amount is",x)