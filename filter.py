# a=[i for i in range(7)]
# v=list(filter(lambda x:x%2==0,a))
# print(v)
# print(a)
# b=[i for i in range(20)]
# c=list(filter(lambda x:x<=10 and x>=5,b))
# print(c)

# a=["apple","banana","mango","manga"]
# for i in a:
#     h=0
#     for j in range(len(i)):
#         if i[j]=="a":
#             h+=1
#         if h>=2:
#             print(i) 
#             break   
s=["apple","mango","banana"]
a=list(filter(lambda x:x.count("a")>=2,s))
print(a)