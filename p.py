"""n=int(input("enter no.of lines: "))
i=1
while i<=n:
    print("*"*i)
    i+=1 

n=int(input("enter no.of lines: "))
i=n
while i>=1:
    print("*"*i)
    i-=1 

n=int(input("enter no.of lines: "))
for i in range(1,4):
    print("*"*i) """
  
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
        print()  