# x=[1,2,3,4,5]
# b=0
# c=len(x)-1
# for i in range(len(x)):
#     x[c]=x[i]
#     x.remove(x[b])
#     if len(x)==b:
#         break
    
# print(x)

# x=[1,2,3,4,5]
# y=[]
# c=0
# b=len(x)-1
# for i in range(len(x)):
#     c=x[b]
#     y.append(c)
#     b-=1
# print(y) 

# for i  in range(len(x)-1,-1,-1):
#     y.append(x[i])    
# print(y)    


# a=[7,8,9,10,11]
# for i in range(len(a),1,-1):
#     a[]

x=[1,2,3,4,5]
y=0
z=len(x)-1
a=0
b=0
c=len(x)/2-1
r=round(c)
for i in range(len(x)):#we can use r
    a=x[y]
    b=x[z]
    x[z]=a
    x[y]=b
    y+=1
    z-=1
    if(y>z):
        break
print(x)


# x=[1,2,3,4,5]
# y=x.copy()
# a=len(x)-1
# for i in range(len(x)):
#     x[i]=y[a-i]
# print(x)    

# x=[]