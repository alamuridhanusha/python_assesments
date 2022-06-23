x="Helloworld"
print(x[::2])
print(x[:3])
print(x[7:])
print(x[:7])
print(x[9])
print(x[2:4])
d=[1,2,3,4]
e=bytes(d)
print(type(e))
h=[2,6,7,8,9]
f=bytearray(h)
print(type(f))
f[0]=10
for i in f:
    print(i,end=" ")

