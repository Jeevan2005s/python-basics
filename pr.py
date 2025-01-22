a=input("enter the weights:")
b=a.split(" ")
b.sort(reverse = True)
c=0
for i in range (len(b)):
  c+=int(b[i])
c/=2
print(c)
p,q=0,0
for i  in  range (len(b)):
  if p<q:
    p+=int(b[i])
  else:  
    q+=int(b[i])  
print(p)
print(q)    