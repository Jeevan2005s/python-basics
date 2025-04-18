class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Add(root,data):
        if root is None:
            return BinaryNode(data)
        if root.data <data:
                root.right = BinaryNode.Add(root.right, data)
        else:
                root.left = BinaryNode.Add(root.left, data)
        return root   
    def Print(root):
        if root:
            BinaryNode.Print(root.left)
            print(root.data,end=" ")
            BinaryNode.Print(root.right)
root=None
d=[45,13,46,12,30,19,28,59,10]
for i in d:
    root=BinaryNode.Add(root,i)    
BinaryNode.Print(root)