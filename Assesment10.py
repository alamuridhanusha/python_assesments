'''n=int(input('Enter n value :'))
num=1
for i in range(0,n):
    for j in range(0,i+1):
        print(num, end=' ')
        num=num+1
    print()'''

'''n=input('Enter n value:')
m=input('Enter m value:')
if(len(n)==len(m)):
    if(n==m):
        print('Both are equal')
    else:
        print("Both are not equal")
else:
    print("Not equal")'''

'''n=int(input('Enter n value:'))
x=0
y=1
count=0
if(n==0):
    print(x)
elif(n==1):
    print(y)
else:
    print('Fibonacci series are:')
    while(count<n):
        print(x)
        z=x+y
        x=y
        y=z
        count+=1'''

'''n=int(input('Enter n value:'))
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            print(n,'is not prime number')
            break
    else:
        print(n,'is prime number')
else:
    print(n,'not prime number')'''

'''X=[11,43,67,99,22,223]
res=[]
for i in X:
    t=i
    s=0
    while(t>0):
        r=t%10
        s=s*10+r
        t=t//10
        if(s==i):
            print(i)
            res.append(i)
print(res)
print(max(res))'''

'''x=input('Enter x value:')
for i in range(0,len(x)):
    for j in range(0,i+1):
        print(x[j],end=' ')
    print()'''

X=[11,43,67,999,22,223]
X.sort()
print(sorted(X)[-2])













