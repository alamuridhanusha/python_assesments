#remove duplicate elements from list
'''x=[1,2,3,4,1,2,5,6]
x=set(x)
x=list(x)
print(x)'''

#count the each ele how many times it is exits
'''x=[1,2,3,4,1,2,5,6]
y=set(x)
out=[]
for i in y:
    if i in x:
        out.append(i)
        out.append(x.count(i))
print(out)'''


#sort the list without sort function  # use any sorting logic
'''x=[10,2,4,3,5]
x=sorted(x)
print(x)'''

#print only even numbers using list comphreension
'''x=[1,3,2,4,5,7,6,8]
y=[i for i in x if i%2==0]
print(y)'''

# wap to print even and its position in another list
'''x=[1,3,2,4,5,7,6,8]
out=[]
for i in range(len(x)):
    if(x[i]%2==0):
        out.append(x[i])
        out.append(x[i)
print(out)'''

