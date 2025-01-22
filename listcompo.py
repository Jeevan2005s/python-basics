x=[1,2,3,4,5]
# y=[i**2 for i in x]
# print(y)
# a=lambda x:x**2
# print(a(5))
z=[i**2 if i%2==0 else i for i in x ]
print(z)