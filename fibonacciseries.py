# #own code
# def fibonacci(i,j,a,y):
#     if a==0:
#         return y
#     y.append(i)
#     i,j=j,i+j
#     a-=1
#     fibonacci(i,j,a,y)
#     return y
# s=int(input("Enter the number of elements you want:"))
# print(*fibonacci(0,1,s,[]))

#modified code for find the last number of the given fibonacci series

def fibonac(n):
    if n==0:
        return "invalid"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonac(n-1)+fibonac(n-2)    
print(fibonac(9))
   
