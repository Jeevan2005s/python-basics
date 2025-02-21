#program to find the square in a list
# a=int(input("enter the length of the array:"))
# b=list(map(int,input().split()))
# x=0
# for i in b:
#     y=int(i/2)
#     while True:
#         if y**2==i:
#             x+=1  
#         y-=1 
#         if y==0:
#             break   
# print(x)            

b=list(map(int,input().split()))
y=0
for i in b:
    print(i**0.5)
    if int(i**0.5)**2==i:
        y+=1

print(y)        