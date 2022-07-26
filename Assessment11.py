'''x="my name is laxmi"
s=x.split()[::-1]
print(' '.join(s))'''

'''x=input('Enter string:')
max=x.count(x[0])
y=set(x)
for i in y:
    if i in x:
        if x.count(i)>max:
            max=x.count(i)
            print("max ele, count",i,x.count(i))'''


'''x="Hello Rama NagA is Good RA"
y=x.split()
for i in range(len(y)):
    if y[i].endswith('A')==True:
        print(y[i],end=' ')'''

'''x='1234'
print(int(x))'''

'''x='Amma is MadaM'
x=x.split()
out=[]
for i in range(len(x)):
    temp=x[i]
    temp=temp[::-1]
    if(temp==x[i]):
        out.append(temp)
print(out)'''

'''x="Hello Kasi Your SalaRy is $10000"
lower,upper,digit,special=0,0,0,0
for i in range(len(x)):
    if(x[i].islower()):
        lower+=1
    elif(x[i].isupper()):
        upper+=1
    elif(x[i].isdigit()):
        digit+=1
    else:
        special+=1
print("Lower case letters count is :",lower)
print("Upper case letters count is :",upper)
print("Numbers count is :",digit)
print("Special chacters count is :",special)'''

'''x=input("Enter string :")
sum=0
for i in range(len(x)):
    sum=sum+ord(x[i])
print(sum)'''

'''z=input('Enter string:')
x=input('Enter character')
print(z.count(x))'''

'''x='Hello World'
y=x.split()
print(y)
res=[]
for i in y:
    res = (y[0].lower(),y[-1].upper())
print(res)'''



'''for i in range(2.0):
    print(i)'''

#print("abcdef".find("cd") == "cd" in "abcdef")
'''x='abcd'
for i in x:
    print(i.upper())'''

'''x=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
for i in x:
    y=sum(i)
    temp=y
    print(y)'''

'''x='hellO worlD'
y=x.split()
y=x.title()
for i in range(-1,len(x)):
    y[i].lower()
print(''.join(y))'''











































