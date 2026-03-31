#1
x=open("write1.txt","w")
x.write("hello guys")
x.write("fun fun")
x.close()
#2
x=open("write1.txt","w")
x.write("this is added at end.\n")
x.close()
#3
x=open("write1.txt","w")
lines=[
    "python python\n",
    "error\n"
]
x.writelines(lines)
x.close()