class college():
  def __init__(x):
    x.bse=[]
  def add(x,n):
     x.bse.append(n) 
  def change(x,n,m):
     for i in x.bse:
        if i.st_name==n:
           i.change_my_mark(m)   
  def remove(x,w):
     for i in x.bse:
        if i.st_name==w:
           x.bse.remove(i)            
class student():
  def __init__(self,name,age,marks):
    self.st_name=name
    self.st_age=age
    self.st_marks=marks
  def change_my_mark(self,m):
       self.st_marks=m 
z=college()
i=1
while i>0:
        name=input("enter student name:")
        age=int(input("enter your age:"))
        marks=int(input("enter your mark:"))
        globals()[f"x{i}"]=student(name,age,marks)
        z.add(globals()[f"x{i}"])
        x=input("do you want to add students:")
        i+=1
        if x=="no" or x == "No":
           break
        elif x.lower()=="yes":
          continue
q=input("do you want change any student's mark:")
if q.lower()=="yes":
   n=input("enter student's name to change mark:")
   m=input("enter new mark:")
   z.change(n,m)
e=input("do you want to remove any students data:")
if e.lower()=="yes":
   w=input("enter students name to remove:")   
   z.remove(w)
print("NAME      AGE  MARK")   
for u in z.bse:
  print(u.st_name      ,u.st_age  ,u.st_marks)

