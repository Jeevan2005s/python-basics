x=10
def ch():
    global x
    x=12
print(x)
ch()
print(x)    

def p():
    a=10
    print(a)
    def ph():
        nonlocal a
        a=23
    ph()    
    print(a)    
p()            
        