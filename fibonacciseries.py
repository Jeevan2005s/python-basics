def fibonacci(i,j,a,y):
    if a==0:
        return y
    y.append(i)
    i,j=j,i+j
    a-=1
    fibonacci(i,j,a,y)
    return y
s=int(input("Enter the number of elements you want:"))
print(*fibonacci(0,1,s,[]))


# def fib(a):
#     l=[0,1]
#     i,j=0,1
#     if a==0 or a==1:
#         return l[a]
#     while len(l)<=a:
#         l.append(l[i]+l[j])
#         i+=1
#         j+=1
#     return l[-1]
# a=int(input("Enter the number of elements you want:"))
# print(fib(a))    
