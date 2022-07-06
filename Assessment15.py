#what is class and object and write an example
#class: collection of objects,variables and methods

'''class A:
    def python(self,x,y):
        print(x,y)
obj=A()
obj.python(10,20)'''

#what is constructor and use with example
#constructor is a special method in python the name of constructor should be __init__(self) method
# constructor will execute automatically when we create a object and main purpose of constructor is to declare and intialize variables.
#constructor is executed only once

'''class B:
    def __init__(self):
        self.a=10
        self.b=100
        print(self.a,self.b,self.a+self.b)
    def python(self):
        print(self.a,self.b)
    def key(self):
        print(self.b)
x=B()
x.python()
x.key()'''

#what is the diff b/w instance method,static method and class method
'''class z:
    y=10
    def __init__(self):
        self.a=10
        self.b=20
        print(self.a,self.b)
    def hai(self):
        self.c=10
        print(self.c)
        print(self.a, self.b)
    @classmethod
    def hello(cls):
        cls.h=40
        z.j=90
        print(cls.h,z.j)
        print(z.y)
    @staticmethod
    def python():
        z.d=60
        print(z.d)
        print(z.y)
obj=z()
obj.hai()
z.hello()
z.python()'''

#how to access one class data into another class
'''class s:
    x=90
    def __init__(self,p,q):
        self.p=p
        self.q=q
    def python(self):
        print(self.p)
        print(self.q)
class d:
    def hai(self,obj):
        obj.p=20
        print(obj.p,obj.q)
        obj.python()
obj1=s(10,90)
obj1.python()
obj2=d()
obj2.hai(obj1)'''

#what is inner class and how to access inner class data write two methods
#method 1:
'''class A:
    def __init__(self):
        print("hai hello")
        self.obj=self.B()
        self.obj.sql()
        self.obj.C()
    def python(self):
        print('Hello python')
    def java(self):
        print('hello java')
    class B:
        def __init__(self):
            print('class B')
        def C(self):
            print("Hai C")
        def sql(self):
            print('Hai sql')
obj1=A()
obj1.python()
obj1.java()'''

#method 2:
'''class A:
    def __init__(self):
        print("hai hello")
    def python(self):
        print('Hello python')
    def java(self):
        print('hello java')
    class B:
        def __init__(self):
            print('class B')
        def C(self):
            print("Hai C")
        def sql(self):
            print('Hai sql')
obj1=A()
obj1.python()
obj1.java()
obj2=obj1.B()
obj2.C()
obj2.sql()'''


#what is refernce variable how to acess data using that
# object is the refernce varibale to access data from the class by using class name.
# syntax: object_name=class_name()













