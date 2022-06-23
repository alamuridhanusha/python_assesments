'''x=[5,10,10,40]
l=len(x)-2
s=0
while(0<l):
    s=s+x[l]
    l+=1
print(s)'''


'''n=int(input('enter n value'))
s=0
temp=n
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
print(s)'''

'''n=int(input('Enter n value :'))
if(n%2==0):
    print('Given number %d is even'%n)
else:
    print('Given number %d is odd'%n)'''

'''n=int(input('Enter n value: '))
for i in range(n,0,-1):
    print(i,end=" ")'''

'''n=int(input('Enter n value: '))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
'''

'''n=int(input('Enter n value: '))
y=1
for i in range(1,n+1):
    y=y*i
print(y)'''

'''n=int(input('Enter n value: '))
print('The factors of given number are:')
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")'''

'''x=[10,1,2,3,100]
n=len(x)
temp=x[0]
x[0]=x[n-1]
x[n-1]=temp
print(x)'''

x=[1,2,10,3,20,4]
a,b=0,0
for i in range(0,len(x)):
    if(x[i]%2==0):
       a+=x[i]
    else:
       b+=x[i]
print('sum of even numbers in list %d'%a)
print('sum of odd numbers in list %d'%b)






