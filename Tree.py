class Tree:
    def __init__(self,data):
        self.data=data
        self.children=[]
    def Add(self,childnode):
        self.children.append(childnode)
    def PrintTree(self):
        print(self.data)
        for child in self.children:
            child.PrintTree()

d=Tree("School")
c1=Tree(10)
c2=Tree(11)
c3=Tree(12)
d.Add(c1)
d.Add(c2)
d.Add(c3)
c1.Add(Tree("a"))
c1.Add(Tree("b"))
c1.Add(Tree("c"))

c2.Add(Tree("a"))
c2.Add(Tree("b"))
c2.Add(Tree("c"))

c3.Add(Tree("a"))
c3.Add(Tree("b"))
c3.Add(Tree("c"))

d.PrintTree()

