try:
 num1=int(input("enter number: "))
 num2=int(input("enter number: "))
 result=num1/num2
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("enter a valid number")
else:
    print("division successfully: ",result)
finally:
    print("this will always run")        
