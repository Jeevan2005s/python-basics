# class car():
#     name="BMW"
#     def on(x):
#         print("engine is on")
#     def off(y):
#         print("engine is off")    
# car().on()        

# class student():
#   def __init__(self,name,age,marks):
#     self.st_name=name
#     self.st_age=age
#     self.st_marks=marks
#   def percentage(self):
#         print(self.st_name," mark is",self.st_marks)      
# x=student("jeevan",19,600)
# y=student("vijay",24,123)
# x.percentage()
# y.percentage()

# class students():
#     def __init__(self):
#       self.st_list=[]  
#     def collect(self):
#       b=int(input("enter the number of students:"))   
#       for i in range(b):
#         name=input("enter student name:")
#         age=int(input("enter your age:"))
#         details={"name":name,"age":age}
#         self.st_list.append(details)
# o= students()
# o.collect()
# print(o.st_list)

class students():
    def __init__(self):
      self.st_list=[]  
    def collect(self):  
      i=2
      while i>1:
        name=input("enter student name:")
        age=int(input("enter your age:"))
        details={"name":name,"age":age}
        self.st_list.append(details)
        x=input("do you want to add students:")
        if x=="no"or"No":
           break
        else:
           continue
o= students()
o.collect()
print(o.st_list)




         