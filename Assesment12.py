# unique elements in string
'''s=input('Enter string: ')
s=set(s)
print(s)'''

#First letter Captial using title()
'''str=input('Enter string: ')
print(str.title())'''

#reversing string
'''str=input('Enter string: ')
print(str[::-1])'''

#printing string or list n times
'''str=input('Enter a string: ')
lst=[1,2,3,4]
n=int(input('Enter n value:'))
print(str*n,end=' ')
print(lst*n,end=' ')'''

#combining list of strings in to single string
'''str=['python',' is',' good',' language']
for i in str:
    str=''.join(str)
print(str)'''

#swap values between two variables
'''x=int(input('Enter x value: '))
y=int(input('Enter y value: '))
temp=x
x=y
y=temp
print('x value is: ',x)
print('y value is: ',y)'''

#split string in to list of sub strings
'''x=input("Enter x value:")
print(x.split())'''

#list comprehension
'''x=[1,2,3,4]
x=[i*i for i in x]
print(x)'''

#palindrome or not
'''x=['amma','hey','apple','madam']
out=[]
for i in range(len(x)):
    temp=x[i]
    temp=temp[::-1]
    if(x[i]==temp):
        out.append(temp)
print(out)'''

#two strings are anagrams(ascii values are equal)
'''x=input('Enter x value:')
y=input('Enter y value:')
if(len(x)==len(y)):
    if (sorted(x) == sorted(y)):
        print('Two strings are anagrams')
    else:
        print("Not anagrams")
else:
    print("Not anagrams")'''

#frequency of elements in list
'''x=['A','H','A','H','S','A']
for i in set(x):
    if i in x:
        print(i,x.count(i))'''






#x=(10,2,3,5)-> each ele multifly by 10   (100,20,30,50)
x=(10,2,3,5)
x=list(x)
y=[i*10 for i in x]
print(y)

# x=[1,2,3,4] -> [3,5,7]
'''x=[1,2,3,4]
for i in range(len(x)-1):
    x[i]=x[i]+x[i+1]
    print(x[i],end=' ')'''


'''str='w3resource'
d={}
for i in str:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print('Count of letters in str are: ',d)'''

















