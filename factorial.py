def fact(a):
    if a==1 or a==0:
        return 1
    # print("a",a)
    # print(a*fact(a-1))
    return a*fact(a-1)
print(fact(5))