# x=[5,6,7,1,2,3,4]
# x.remove(1)
# x.insert(0,1)
# print(x)

x=[5,6,7,1,12,13,14,2]
y=x.copy()
z=1
v=2
a=y.index(z)
b=y.index(v)
for i in range(len(x)):
    if y[i]==z:
        x[0]=z
    elif y[i]==v:
        x[a+1]=v
    else:
       x[i+1]=y[i]
print(x)

# x=[5,6,7,1,12,13,14,2]
# y=x.copy()
# a=y.index(1)
# b=y.index(2)
# for i in range(len(x)):
#     if i==0:
#         x[i]=1
#     elif i==a+1:
#         x[i]=2
#     elif i<=b:
#         x[i]=y[i-1]

# print(x)


