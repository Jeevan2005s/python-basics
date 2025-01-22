data=[{"name":"jeevan","password":1234,"age":19,"salary":20000,"noofleave":0,"position":"employee","reason":[]},
      {"name":"pandi","password":5678,"age":19,"salary":20000,"noofleave":0,"position":"employee","reason":[]},
      {"name":"magesh","password":91011,"age":20,"salary":20000,"noofleave":8,"position":"employee","reason":[]},
      {"name":"arun","password":2345,"age":20,"salary":50000,"noofleave":0,"position":"HR","reason":[]},
      {"name":"varun","password":3456,"age":20,"salary":100000,"noofleave":4,"position":"manager","reason":[]},
      {"name":"tharun","password":4567,"age":20,"salary":200000,"noofleave":0,"position":"admin","reason":[]}
      ] 
prvdata=[{"email":"jeevan@gmail.com","password":1234,"position":"employee"},
         {"email":"pandi@gmail.com","password":5678,"position":"employee"},
         {"email":"magesh@gmail.com","password":91011,"position":"employee"},
         {"email":"arun@gmail.com","password":2345,"position":"HR"},
         {"email":"varun@gmail.com","password":3456,"position":"manager"},
         {"email":"tharun@gmail.com","password":4567,"position":"admin"},]
CA=1000000      
class employee:
    def details(self):
        print(self.data[self.indexOfCurrentUser]["name"])
        print(self.data[self.indexOfCurrentUser]["age"])
        print(self.data[self.indexOfCurrentUser]["salary"])
    def inform(self,day,reason):
       data[self.indexOfCurrentUser]["noofleave"]+=day
       data[self.indexOfCurrentUser]["reason"].append(reason)   
       print("your leave date added")
    def noof(self):         
          print(data[self.indexOfCurrentUser]["noofleave"])   
          
class Hr(employee):
    def detailss(self):
        print(self.data[self.indexOfCurrentUser]["name"])
        print(self.data[self.indexOfCurrentUser]["age"])
        print(self.data[self.indexOfCurrentUser]["salary"])
    def check_leave(self,name):
      for i in range(len(data)): 
         if name == data[i]["name"]:
           self.index=i  
           print( print(data[self.index]["noofleave"]))
         else:
          print("there is no employee in the given name")  
    def full(self):
      for i in range(len(prvdata)):
        if prvdata[i]["position"]=="employee":
          print(data[i])     

class manager(Hr):
    def detail(self):
        print(self.data[self.indexOfCurrentUser]["name"])
        print(self.data[self.indexOfCurrentUser]["age"])
        print(self.data[self.indexOfCurrentUser]["salary"])
    def fulemp(self):
      for i in range(len(prvdata)):
        if prvdata[i]["position"]=="employee":
          print(data[i])  

    def fulhr(self):
      for i in range(len(prvdata)):
        if prvdata[i]["position"]=="HR":
          print(data[i])       
    def rem(self,name):
      for i in range(len(data)):
        if name == data[i]["name"] and data[i]["position"]=="employee":
          prvdata.remove(prvdata[i])
          data.remove(data[i]) 
          return(True)  

    def prom(self,name):
      for i in range(len(prvdata)):
        if data[i]["name"]==name:
          if prvdata[i]["position"]=="employee":
            prvdata[i]["position"]="HR"
            data[i]["position"]="HR"
            data[i]["salary"]=50000  
          else:
            print("there is no employee in the given name")        
class admin(manager):
    def __init__(self,data,prvdata):
        self.data=data
        self.prvdata=prvdata 
    def lg(self,email,password):
      for i in range(len(prvdata)):
         if email == prvdata[i]["email"] and password == prvdata[i]["password"]:
           self.indexOfCurrentUser = int(i)
           return prvdata[i]["position"]
      print("login failed, your data does not matches")    
    def add(self,a):
        name=input("enter the employee name:")
        age=int(input("enter age:"))
        email=input("enter email:")
        password=int(input("enter password:"))
        salary=int(input("enter salary:"))
        d={"name":name,"password":password,"age":age,"salary":salary,"noofleave":0,"position":a,"reason":[]}
        f={"email":email,"password":password,"position":a}       
        data.append(d)
        prvdata.append(f)  
        print(a,"data added")   
    def det(self):
        print(self.data[self.indexOfCurrentUser]["name"])
        print(self.data[self.indexOfCurrentUser]["age"])
        print(self.data[self.indexOfCurrentUser]["salary"])
    def emp(self):
      for i in range(len(prvdata)):
        if prvdata[i]["position"]=="employee":
          print(data[i])  
    def hr(self):
      for i in range(len(prvdata)):
        if prvdata[i]["position"]=="HR" or prvdata[i]["position"]=="manager":
          print(data[i])       
    def remm(self,name):
      for i in range(len(data)):
        if name == data[i]["name"] and (data[i]["position"]=="employee" or data[i]["position"]=="HR"):
          prvdata.remove(prvdata[i])
          data.remove(data[i]) 
          return(True)
    def promm(self,name):
      for i in range(len(prvdata)):
        if data[i]["name"]==name:
          if prvdata[i]["position"]=="employee":
            prvdata[i]["position"]="HR"
            data[i]["position"]="HR"
            data[i]["salary"]=50000 
            print("the employee has been promoted to HR")       
          elif prvdata[i]["position"]=="HR":
            prvdata[i]["position"]="manager"
            data[i]["position"]="manager"
            data[i]["salary"]=100000
            print("the HR has been promoted to manager")
          else :
            print("there is no person in the given name")
o=admin(data,prvdata) 
while True:
  i=input("do you want to login:")  
  if i=="yes":
    email=input("enter your email id:")
    password=int(input("enter your password:"))
    p=o.lg(email,password)
    if p == "employee":
           print("login sucessfull")
           while True:
              print("""enter the option you want to choose:
                1.To print my details
                2.To inform leave
                3.To see my total leave days
                """)
              r=int(input("Enter option:"))
              if r==1:
                  o.details()
              elif r==2:
                  d=int(input("enter the no of leave days you want:"))
                  y=input("enter the reason:")
                  o.inform(d,y)   
              elif r==3:
                  o.noof() 
              else :
                  break
    elif p=="HR":
           print("login sucessfull")
           while True:
              print("""enter the option you want to choose:
                1.To print my details
                2.To check leave
                3.To add employee
                4.To see employee list
                """)
              r=int(input("Enter option:"))
              if r==1:
                  o.detail()
              elif r==2:
                  d=input("enter the name of emloyee:")
                  o.check_leave(d)   
              elif r==3:
                  a="employee"
                  o.add(a)
              elif r==4:
                 o.full()    
              else :
                  break      
    elif p=="manager":
           print("login sucessfull")
           while True:
              print("""enter the option you want to choose:
                1.To print my details
                2.To check employee stats
                3.To remove employee
                4.To promote employee
                5.To see HR stats
                6.To add employee or HR
                """)
              r=int(input("Enter option:"))
              if r==1:
                  o.detailss()
              elif r==2:
                  o.fulemp()   
              elif r==3:
                  a=input("enter the employee name:")                
                  t=o.rem(a)
                  if t==True:
                    print("the employee has been removed")
                  else :
                    print("there is no employee in the given name")  
              elif r==4:
                  a=input("enter the employee name:") 
                  print("the employee has been promoted to HR")
                  o.prom(a)
              elif r==5:
                  o.fulhr()  
              elif r==6:
                r=input("do you want to add employee or HR :")
                if r!="manager" and r!="admin":
                 o.add(r)  
                else:
                  print("you can only add employee and HR")    
              else :
                  break   
    elif p =="admin":
            print("login sucessfull")
            while True:
              print("""enter the option you want to choose:
                1.To print my details
                2.To check employee stats
                3.To see HR and manager stats
                4.To remove employee or HR
                5.To promote employee or HR
                6.To update salary
                7.To credit salary
                8.To check company amount
                9.To add employee or HR or manager
                """)
              r=int(input("Enter option:"))
              if r==1:
                  o.det()
              elif r==2:
                  o.emp()   
              elif r==3:
                o.hr()    
              elif r==4:
                  a=input("enter the name to remove:")                
                  t=o.remm(a)
                  if t==True:
                    print("the person has been removed")
                  else :
                    print("there is no person in the given name")  
              elif r==5:
                  a=input("enter the name:") 
                  o.promm(a) 
              elif r==6:
                t=input("do you want to update emoployee salary:")
                if t=="yes":
                  for i in range(len(data)):
                    u=data[i]["noofleave"]
                    while u>3 and data[i]["position"]!="admin":
                      data[i]["salary"]-=200
                      u-=1
                print("the new salary has updated")      

              elif r==7:
                y=0
                for i in range(len(data)):
                  if data[i]["position"]!="admin":
                    y+=data[i]["salary"]
                    print(data[i]["name"])
                    print(data[i]["salary"])
                print("the total salary for employee,hr and manager is:",y)
                r=input("do you want to credit salary:")
                if r=="yes":
                  CA-=y    
                  print("salary has credited")
                else:
                  continue  
              elif r==8:
                print(CA)
                e=input("do you want to add funds to company amount:")
                if e=="yes":
                  e=int(input("enter the amount you want to add:"))
                  CA+=e
                  print("Updated Company Amount:",CA)
                else:
                  continue
              elif r==9:
                r=input("do you want to add employee or HR or manager :  ")
                if r!="admin":
                  o.add(r)   
                else:
                  print("you are not able tp add admin")   
                
              else :
                  break              
  else: 
    print("login failed")    
    break