a="Jeevan"
print(len(a))
#casting(changes the data type)
b=29
y=str(b)
print(a.upper())
print(a.lower())
print(a.capitalize())
b="jeevan prasad"
print(b.title())
b="   a   "
print(b.strip())
c="jeevan prasad"
print(c.split("a"))
c=["divya","bharathi"]
print(" ".join(c))
d="hello world"
print(d)
print(d.replace("world","there"))
print(d.find("or"))
print(d.count("l"))


a="jeevan prasad"
b=(a.replace(" ","_"),a.replace("j","J"))
print(b)