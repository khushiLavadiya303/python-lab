# 1.integer array
'''from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr))
#2.len()
from array import array
arr=array('i',[22,33,44,55,66,77])
print(len(arr))
#3.append()
from array import array
arr=array('i',[1,2])
arr.append(3)
print(arr)
#4.insert()
from array import array
arr=array('i',[1,2,4])
arr.insert(2,3)
print(arr)'''
#5.remove()
from array import array
arr=array('i',[1,2,3,4,3,5,3])
arr.remove(3)
print(arr)
#6.pop()
from array import array
arr=array('i',[1,3,4,5])
x=arr.pop()
print("removed: ",x)
print(arr)
#7.index(x)
from array import array
arr=array('i',[1,2,3,4,5])
print(arr.index(4))
#8.count(x)
from array import array
arr=array('i',[1,2,3,4,3,5])
print(arr.count(3))
#9.reverse()
arr=array('i',[10,20,30,40,50])
arr.reverse()
print(arr)
