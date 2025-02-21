a=int(input("enter the number:"))
b=list(map(int,input().split()))
q=int(input())
p=int(input())
e,r=0,0
while True:
   for i in range(len(b)):
      if i==r:
         b[i]=b[i]-q
         if b[i]<0:
            b[i]=0
      else:
         b[i]=b[i]-p
         if b[i]<0:
            b[i]=0
   r+=1      
   e+=1
   if sum(b) ==0:
      break
print(e)   
           
