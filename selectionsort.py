def selection_sort(a):
    for i in range(0,len(a)-1):
        m =i
        for j in range(i,len(a)):
            if a[j]<a[m]:
                m=j
        a[i],a[m]=a[m],a[i]
    return a
arr=list(map(int,input().split()))
print(*selection_sort(arr))

            