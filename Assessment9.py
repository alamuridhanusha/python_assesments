'''for i in range(1,10):
    if(i==5):
        continue
    elif(i==8):
        break
    else:
        print(i,end=' ')
else:
    print('Hello')'''

'''x=[121,77,443,111,223,675]
for i in x:
    t=i
    s=0
    while(t>0):
        r=t%10                                                                
        s=s*10+r
        t=t//10
        if(s==i):
            print(i)'''

'''x=[1,2,3,2,3,4,5]
result=[]
for i in x:
    if i not in result:
        result.append(i)
print(result)'''

n=int(input('Enter n value:'))
temp=n
for i in range(1,n):
    print('*'*(n-1))
    n=n-1
for i in range(1,temp):
    print('*'*(temp-2))
    temp=temp-1


'''n=int(input('Enter n value: '))
for i in range(1,(n+1)):
    print('*'*(n-1), end=' ')
    print()
print('*'*(n-2),end=' ')'''


'''for i in range(1,11):
    print('Multiplication table for %d is:' %i)
    for j in range(1, 11):
        print('%d*%d=%d' % (i, j, i * j))'''

'''X=['helo','world','good']
for i in range(len(X)):
    X[i]=X[i].capitalize()
print(X)'''


































