def jp():
    try:
       a=input("enter the input:")
       print(123/int(a))
    except ZeroDivisionError:
        print("cannot divide by zero")
    except ValueError:
        print("unabel to convert alphabets to integer")
    else:
        print("sucefully compeleted")
    finally:
        print("entirely done")
jp()                    

