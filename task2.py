#1-CALCULATE SIMPLE INTEREST
p= float(input("enter principal amount: "))
r=float(input("enter rate of interest: "))
t=float(input("enter time : "))
SI=(p*r*t)/100
print("simple interest is: ",SI)
#2-FIND MAXIMUM OF TWO NUMBERS
a=int(input("enter first number: "))
b=int(input("enter second number: "))
if  a>b:
    print("Maximum number is",a)
else:
    print("Maximum number is",b)   
#3-print number 1 to 5
i=1
while i<=5:
    print(i)
    i=i+1   
#4-find length of a string
text="hello"
length=len(text)
print("length of string: ",length)     
#5-print a welcome message
print("hello welcome to python") 
#6-print 1st character of the string
text="python"
print(text[0]) 
#7-print last character of the string
text="python"
print(text[5]) 
#8-check positive or negative number
num= int(input("enter a number: "))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")  
#9-add three numbers
a=4
b=5
c=8
sum=a+b+c  
print(sum)
#10-take a input from user
a=input("enter : ")
print(a)   