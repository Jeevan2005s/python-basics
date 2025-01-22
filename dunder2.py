import dunders
class beta:
    def __init__(self):
        pass
    def getname(self):
        print("prasad")
    def getdata(self,data):
        self.data=data
b=beta()
b.getname()
a=dunders.alpha()
a.getname()
print(__name__)        
