# class student:
#     def __init__(self,n):
#        self.n=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         value=self.n
#         self.n-=1
#         if value<0:
#             raise StopIteration    
#         return value
# s=student(6)
# for i in s:
#     print(i) 
class alpha:
    def __init__(self):
        pass
    def getname(self):
        print("jeevan")
print(__name__)        