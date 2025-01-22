class library:
   def __init__(self,books):
      self.books=books       
      self.my_books=[]
   def show_books(self):
       print("The available books are:")
       for i in self.books:
          print(i)
   def borrow(self,book_name):
      if book_name in books:
        self.books.remove(book_name)
        self.my_books.append(book_name)
      else :
         print("book is not available")  
   def returrn(self,book_name):
      if book_name in books2:
        self.books.append(book_name)  
        self.my_books.remove(book_name)     
      else :
         print("that is not our book")  
books=["tamil","english","maths","science"]
books2=books.copy()
o=library(books)   
while True:
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
   elif d==3:
      book_name=(input("enter book name:"))
      o.returrn(book_name)
   elif d==4:
      print(o.my_books)      
   else:
      break 
