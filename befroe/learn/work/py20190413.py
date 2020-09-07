
class A():
    def add(self,a,b):
        return a+b
class B(A):
    def sub(self,a,b):
        return a-b
print (B().sub(10,2),B().add(10,2))