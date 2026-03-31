'''a,b,c=map(int,input('enter three numbers'),spilt())
print('the sum is :(a+b+c)')'''
'''n=input('enter a string')
vowels='aeiou'
vowel_count=0
for char in n:
    if char in vowels:
        vowel_count+=1
        print('number of vowels:',vowel_count)'''


'''n=int(input('enter number'))
limit=int(input('enter a max limit'))
i=n
while i<=limit:
    print(i,end=',')
    i+=n'''

'''numbers=[1,2,3,4,5]
double=[]
for num in numbers:
    double.append(num*2)

print('double numbers:',double)'''

''''n=float(input('enter number'))
if n<0:
    n=-n
    print(f'the absolute value is {n}:')'''

'''def evenodd(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'
    print(evenodd(num))'''

def voting_eligibility():
    age=int(input('enter age'))
    if age >=18:
         return'eligible for vote'
    else:
        return'not eligible for vote'
                            

