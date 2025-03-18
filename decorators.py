def pretty(func):
    def inner():
        print("*"*50)
        func()
        print("*"*50)
    return inner
# def r():
#     print("Hello")
# new=pretty(r)
# new()
@pretty
def r():
    print("Hello")
r()