college=[{10:[{"name":"vicky","age":19,"marks":{"T":100,"E":98}},
              {"name":"venkat","age":19,"marks":{"T":92,"E":93}}]}]
print(college[0][10][1]["marks"]["E"])


x={"name":"jeevan",
   "age":19}
print(x.get("age"))
x.update({"age":20})
print(x)
for i in x.values():
    print(i)
x.pop("age")
print(x)
x.clear()
print(x)
