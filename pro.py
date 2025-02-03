# a=[1,2,3,4,5,6,7,8,9,10]
# c=0
# b=len(a)
# while a[c]<=10:
#     print("*"*b)
#     c+=1
#     b-=1
#     if c==10:
#         break       

# for i in range(10):
#     print("*"*i)


# a=[1,2,3,4,5,6,7,8,9,10]
# c=0
# b=[]
# while c<=10:
#     if a[c]%2==0:
#             d=2
#     else:
#             b.append(a[c])
#     c+=1 
#     print(c)     
# print(b)
i=1
c=0
b=0
while i<=50:
  if i%2==0:  
    b=i**2
    c+=b
  i+=1               
print(c)    

# i=1
# a=1
# while i<=10:
#         i=a*i
#         i+=1
#         a+=1    
#         print(i)