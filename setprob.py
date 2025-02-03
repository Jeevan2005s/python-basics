a=[1,2,3,4,4,5,5]
b=[4,5,6,7,4,5,8]
c=[]
for i in a:
   if i in b and i not in c:
              c.append(i)
print(c)         