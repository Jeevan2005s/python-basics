a=input("Enter the first person's name:")
b=input("Enter the second person's name:")
i=0        
while i<len(a):
    if a[i] in b:
        b=b.replace(a[i],"",1)
        a=a[:i]+a[i+1:]
        i=0
    i+=1
c=len(a)+len(b)
flames=["f","l","a","m","e","s"]
while len(flames)>1:
    index=(c%len(flames))-1
    if index >=0:
        flames=flames[index+1:]+flames[:index]
    else:
        flames.pop()
k=flames[0]
h={"f":"Friends","l":"Love","a":"Affection","m":"Marriage","e":"Enemies","s":"Siblings"}
print(f"The relationship between two persons is:{h[k]}")                