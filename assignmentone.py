x="hello humans"
print(x)
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
sum_result = float(num1) + float(num2)
print("The sum of", num1, "and", num2, "is:", sum_result)
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")
year=int(input("enter a year: "))
if year %4==0:
  print("lap year")
else:     
 print("not a leap year")  
PI=3.14
 print(PI)
num=int(input("enter a number: "))
print("square:",num**2) 
radius=float(input("enter the radius of the circle: "))
area=3.14*radius*radius
print("area of circle: ",area)
data=input("enter anything")
print("data type is: ",type(data))
import math
angle = 90
radians = math.radians(angle)
print(f"Sine of 90 degrees: {math.sin(radians)}")
import math
base = 5
exponent = 3
result = math.pow(base, exponent)
print(f"{base} to the power of {exponent} is {result}")
number = float(input("enter a number: ")) 
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")