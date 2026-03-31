#1.basic keyword
def student_info(name,age,city):
    print("name: ",name)
    print("age: ",age)
    print("city: ",city)
student_info(age=19,city="mumbai",name="alice")  
#2.mixing pos and key
def display(a,b,c):
    print("a= ",a)
    print("b= ",b)
    print("c= ",c)
display(2,c=4,b=3)
#3.simple int
def simple_interest(P:float,r:int,t:float):
    si=(p*r*t)/100
    print("simple interest: ",si)
simple_interest(p=5000,t=5,r=1.6)
simple_interest(t=1.5,p=5000,r=3)          
    