x=[{"name":"soap","rate":50},
   {"name":"speaker","rate":1000},
   {"name":"rice","rate":90}]
b=list(map(lambda x:{"name":x["name"],"rate":x["rate"]-(x["rate"]/100)*25} if x["rate"]>100 else x,x))
print(b)