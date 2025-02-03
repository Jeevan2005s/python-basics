# s=[7,3,4,5,7,3,2,6,7,3]
# a=0
# b=0
# for i in s:
#     x=s.index(7,a,b)
#     print(x)
#     a+=1
#     b+=1

# s=[7,3,4,5,7,3,2,6,7,3]
# a=0
# for i in s:
#     if 7 in s[i:]:
#         c=s.index(7,a)
#         a+=1
#         print(c)

        #above  is partially wrong

s=[7,3,4,5,7,3,2,6,7,3]
a=-1
b=7
for i in range(s.count(b)):
    c=s.index(b,a+1)
    print(c)
    a=c