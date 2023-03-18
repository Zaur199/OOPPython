import timeit

class A:
    __slots__ = ("a", "b")
#a = A()
#a.a = 1
#print(a.a)
#print(a.__slots__)

class B(A):
    __slots__ = ("c", "f") 

b = B()
#b.a = 1
b.c = 1
print(b.__slots__)  
#print(b.__dict__)  

#def actions(e):
    #e.a = 1000
    #e.b = 2000
    #e.a
    #e.b
    #del e.a
    #del e.b
    
#def test():
    #actions(A())


#print(timeit.repeat(test))
