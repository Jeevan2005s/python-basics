def mergesort(left,right):
    s=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            s.append(left[i])
            i+=1
        else:
            s.append(right[j])
            j+=1
    s.extend(left[i:])
    s.extend(right[j:])
    return s
def merge(list):
    if len(list)<=1:
        return list
    mid=int(len(list)/2)
    l=merge(list[:mid])
    r=merge(list[mid:])
    return mergesort(l,r)
a=list(map(int,input().split()))
sorted_array=merge(a)
print(sorted_array)