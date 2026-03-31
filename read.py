#1.read
"""x=open("read1.txt","r")
data=x.read()
print("file content: ",data)
x.close() 
#2.readline
x=open("read1.txt","r")
line1=x.readline()
line2=x.readline()
line3=x.readline()
print("line1: ",line1)
print("line2: ",line2)
print("line3: ",line3)
x.close() 
#3.readlines
x=open("read1.txt","r")
lines=x.readlines()
print("list of lines: ",lines)
print("numbers of lines: ",len(lines))
x.close() 
#4.reading specific line
x=open("read1.txt","r")
lines=x.readlines()
print(lines[2].strip())
x.close() """
#5.read characters
x=open("read1.txt","r")
data=x.read(5)
print("first: ",data)
x.close()
