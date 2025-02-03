# #prb1 
# x=5
# y=10
# z=15
# if(x<y and y<z or x==5):
#     print("true")
# else:
#     print("false") 
# #prb2
# a=8
# b=3
# c=12
# if(a+b*c>c and c%b==0):
#     print("condtion is true")
# else:
#     print("condition is false")     

# #prb3 
# p=4
# q=2
# if not(p*q==8 or p+q==5):
#     print("true")
# else:
#     print("false")

# #prb4 
# m=7
# n=14
# if (5<m<10<n):
#     print("true")
# else:
#     print("false")

# #prb5
# r=20
# s=5
# t=2
# if(r%s==0 and r/s>t) or (r-s*t<10):
#     print("T")
# else:
#     print("F")

# #prb6
# u=2
# v=3
# w=4
# if(u**v>w and w**u<20 or not(v**2==9)):
#     print("T")
# else:
#     print("F")       

#creating a grade system to represent student grades
i=int(input("Enter the value:"))
print("Grade S") if(i>=90) else print("Grade A") if(i>=80) else print("Grade B") if(i>=70) else print("Grade C") if(i>=35) else print("Fail")                        