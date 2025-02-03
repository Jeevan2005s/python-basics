x=input("")
y=input("")
z=0
for i in range(len(x)):
    x=x[-1]+x[0:len(x)-1]
    for j in range(len(x)):
        if x[j:j+len(y)]==y: 
            z+=j   
print(z)