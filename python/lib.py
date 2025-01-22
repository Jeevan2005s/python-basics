class library:
   def __init__(self,books):
      self.books=books       
   def show_books(self):
       print("The available books are:")
       for i in self.books:
          print(i)
   def borrow(self,book_name):
      if book_name in books:
        self.books.remove(book_name)
      else :
         print("book is not available")  
   def returrn(self,book_name):
      if book_name in books2:
        self.books.append(book_name)       
      else :
         print("that is not our book")  
class users(library):
   def __init__(self,user, books):
      self.user=user
      self.indexOfCurrentUser = -1
      super().__init__(books)
   def login(self,name,password):
      for i in range(len(user)):
        if name == user[i]["name"] and password == user[i]["password"]:
          self.indexOfCurrentUser = i
          return True
      return False
         
   def sign_up(self,name,password,age):
      b={"name":name,"password":password,"age":age} 
      self.user.append(b)
   def brw(self,bookname):
      self.user[self.indexOfCurrentUser]['myBooks'].append(bookname)
   def ret(self,bookname):
      if bookname in self.user[self.indexOfCurrentUser]['myBooks']:
         self.user[self.indexOfCurrentUser]['myBooks'].remove(bookname)      
      else:
         print("you dont have the book")   
   def id(self):
      return self.indexOfCurrentUser
user=[{"name":"jeevan","password":1234,"age":19,"myBooks":[]},{"name":"pandi","password":5678,"age":19,"myBooks":[]},{"name":"magesh","password":91011,"age":20,"myBooks":[]}]         
books=["tamil","english","maths","science","social"]
books2=books.copy()
o=users(user,books)
while True:
 print("""select option
       1.log in
       2.sign up""")
 s=int(input(""))
 if s==1:
  name=input("enter your name:")
  password=int(input("enter your password:"))
  r = o.login(name,password)
  if r:
   print("login successful")
   while 1:
    print("""Enter any options below
            1.diplay all books
            2.to borrow books
            3.to return books
            4.to display your books""")
    d=int(input(""))
    if d==1:
      o.show_books()
    elif d==2:
         book_ame=(input("enter books name you want:"))

         n = book_ame.split(" ")
         for i in range(len(n)):
            if n[i] in books:
               o.borrow(n[i])
               o.brw(n[i])     

    elif d==3:
      book_name=(input("enter book name:"))
      o.returrn(book_name)
      o.ret(book_name)
    elif d==4:
      t=o.id()
      print(user[t]["myBooks"])      
    else:
      break  
  else:
      print("Login failed")
 elif s==2:
   name=input("enter your name:")
   password=int(input("enter your password:"))
   age=int(input("enter your age:"))
   o.sign_up(name,password,age)
 else :
    break   
 
