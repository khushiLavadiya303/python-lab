#1
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#2
rows = 5
for i in range(1, rows + 1):
    print((str(i) + " ") * i)
#3
rows = 5
for i in range(1, rows + 1):
    for j in range(65, 65 + i):  # A=65
        print(chr(j), end=" ")
    print()
#4
rows = 5
for i in range(1, rows + 1):
    print((chr(64 + i) + " ") * i)
