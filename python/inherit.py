class students:
    def details(self):
        print(self.name)
    def __init__(self,name):
        self.name=name 
class det(students):
    pass
o=det("jeevan")
o.details()      
