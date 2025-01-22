a=input("")
vowels=["a","e","i","o","u"]
n=["1","2","3","4","5","6","7","8","9","0"]
S=["&","$","@"]
p,b,c,d=0,0,0,0
for i in a:
    if i  in vowels:
        p+=1
    elif i in n:
        b+=1
    elif i in S:
        c+=1
    else:
        d+=1
print(p)
print(b)
print(c)
print(d)        

# bgfhggf