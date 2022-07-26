import keyword
k=keyword.kwlist
f=open('Assessment2.py','r')
x=f.readlines()
for i in range(len(x)):
    for k in i:
        print(k)
f.close()
