'''a,b=700,600
if(a>b and b!=0):
    print('value of a and b %i %i' %(a,b))'''


'''a,b,c=[int(x) for x in input('Enter three values :').split()]
if((a+b+c)!=10):
    print('values of a,b,c %i %i %i'%(a,b,c))'''

'''p=int(input('enter p value :'))
if(type(p)==str):
    print('p is string type')
else:
    print('p is int type')'''

'''q=bool(input('enter a value: '))
if(q==True):
    print('value of q is %i' %q)
else:
    print('value of q is %i' %q)'''

'''x,y=[str(h) for h in input('enter a value: ').split(',')]
if(len(x)>len(y)):
    print('length of x is greater ')
elif(len(x)<len(y)):
    print('length of y is greater ')
else:
    print('lengths of x and y are equal : %s%s'%(x,y))'''

'''x=int(input('Enter x value: '))
if(x%2==0):
    print('x divisible by 2')
elif(x%3==0):
    print('x divisible by 3')
elif(x%5==0):
    print('x divisible by 5')
else:
    print(x)'''

'''a,b,c,d=[int(x) for x in input('Enter values of a,b,c,d :').split(' ')]
if((a+b)!=(c+d)):
    print('white')
    if((a+b)>5):
        print('green')
    elif((c+d)<10):
        print('yellow')
        if((a+c)<8):
            print('black')
        elif((b+d)>9):
            print('blue')
        else:
            print('red')
    else:
        print('skublue')
else:
    print('orange')'''


x=list(range(1,10))
y=list(range(5,10))
if(x[4]==y[0]):
    print('value is %i %i'%(x[4],y[0]))
    if(x[5]!=y[1]):
        print('values are %i %i'%(x[5],y[1]))
    elif((x[6]==x[2]) or (x[5]==x[1])):
        print(x[6])
    else:
        print(x[8])
else:
    print(y[6])







