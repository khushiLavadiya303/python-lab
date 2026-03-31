'''string=input('enter a string:')
vowels='aeiou'
vowel_count=0
for char in string:
    if char in vowels:
        vowel_count+=1
print('number of vowels',vowel_count)'''
'''for i in range(1,11):
  print(f'square of {i}:{i**2}')'''
'''number=int(input('enter number'))
limit=int(input('enter maximum limit'))
i=number
while i<=limit:
    print(i,end=" ")
    i+=number'''
'''number=[1,2,3,4,5]
double=[]
for num in number:
    double.append(num*2)
print('doubled numbers:',double)'''
'''num=float(input('enter a number:'))
if num<0:
    num=-num
print(f'the absolute value is {num}:')'''
'''string=input('enter a string')
if string.isupper():
    print(f" '{string}' is in uppercase")
elif string.islower():
    print(f" '{string}' is in lowercase")
else:
    print(f" '{string}' contains both uppercase and lowercase characters.")'''
a,b,c=map(int,input('enrter three numbers:'),split())
print('the sum is:(a+b+c)')
