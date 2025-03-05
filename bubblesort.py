a=list(map(int,input().split()))
count=0
c=True
i=len(a)-1
while c:
    c=False    
    for j in range(i):       
        if a[j]>a[j+1]:
           a[j],a[j+1]=a[j+1],a[j]
           c=True
        count+=1    
    i-=1    
print(count)    
print(*a)