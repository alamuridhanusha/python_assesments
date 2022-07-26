#wa function to check wheather num is prime or not
'''def prime(num):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                return False
            else:
                return True
    else:
        False
print(prime(12))
print(prime(3))'''

#types of all functions with examples
#positinal arguments
'''def python(a,b,c):
    print(a+b)
    print(b)
    print(c)
python(10,20,30)'''

#keyword arguments
'''def hello(p,q,r,s):
    a=p+q
    b=r+s
    print(a,b,p,q,r,s)
hello(r=10,p=20,q=30,s=10)'''

#default arguments
'''def good(a,c,h='data structures'):
    print(a)
    print(c)
    print(h)
good('C','Java')
good('C','Python','DBMS')'''

#variable length arguments
'''def func(*a):
    return sum(a),a[2],a[3]+a[1],a[1]
b,c,d,e=func(1,3,4,5,6,7)
print(b)
print(c)
print(d)
print(e)'''

#keyword variable length arguments
'''def python(**a): # formal args
    print(a.keys())
    print(a.items())
    return a
a=python(p=10,q=20,r=30,s=40)
print(a)'''


#x={'A':100,'B':200}   Op: {100:'A',200:'B'}

'''def python():
    x = {'A': 100, 'B': 200}
    new_dict = dict(map(reversed, x.items()))
    print(new_dict)
python()'''

#x=[121,24,55,7,9] -> [121,55] (write function to fetch only palindrom nubers)

'''def palindrome(list_x):
    c=0
    for i in list_x:
        rev=0
        temp=i
        while(i>0):
            r=i%10
            rev=rev*10+r
            i=i//10
        if(temp==rev):
           print('palindrome number is',temp)
           c=c+1
list_x=[121,24,55,7,9]
palindrome(list_x)'''


#x=[1,2,3,5] -> add 10 to each element in list use lambda fun
'''my_list=[1,2,3,5]
new_list=list(map(lambda x:(x+10),my_list))
print(new_list)'''

# what is filter ,reduce map with syntax aand example
#filter-It will take 2 arguments one is function and the other is list and filters the particular elements
#syntax: var_name=list(filter(function,iterable object))
'''my_list=range(1,11)
new_list=list(filter(lambda a:a%2==0,my_list))
print(new_list)'''

#reduce-reduce functions reduces the sequence of elements into single element by applying specified function
#we wanto import Module called Functools to use reduce function
#Syntax: reduce(funtion_name,sequence)

'''from functools import reduce
x=range(1,11)
z=reduce(lambda a,b:a+b,x)
print(z)'''


#map-map will apply on each and every element of list and it will modify every element of list
#syntax: var_name=map(fun_name,sequence)
'''x=list(range(1,11))
z=list(map(lambda a:a%3==0,x))
print(z)'''

#wa function x=[[1,2,3],[4,5,6],[1,2,3]] remove duplicate list from list
'''x=[[1,2,3],[4,5,6],[1,2,3]]
res=list(set(map(lambda i:tuple(sorted(i)),x)))
print(res)'''













