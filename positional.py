#1.basic positional arguments
def add(a,b):
    print("a= ",a)
    print("b= ",b)
    print(a+b) 
result=add(2,5)
print("sum= ",result)
#2,student info
def student_info(name,roll,marks):
    print("name: ",name)
    print("roll no: ",roll)
    print("marks: ",marks)
student_info("alice",1,95)
#3.simple int
def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple interest: ",si)
simple_interest(5000,4,4)
#4.area of circle
def ar_circle(r):
    a_circl=3.14*r*r
    print("area of circle: ",a_circl)  
ar_circle(2.6)
ar_circle(3)
#5.pos or neg
def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero") 
check_value(30)
check_value(0)
check_value(-50)
#6.odd or even 
def odd_even(no):
    if(no%2==0):
        print(f"value {no} is even")
    else:
        print(f"value {no} id odd")
odd_even(25)
odd_even(40) 
#6.arithmetic op
def addition(a,b):
    add=a+b
    print("addition of two values ",add)
addition(20+10.5) 
addition(159,200)          