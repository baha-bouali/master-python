# MRO : Model Resolution Order

class A: 
    def hello(self): print("A");

class B(A):
    def hello(self): print("B"); super().hello()

class C(A):
    def hello(self): print("C"); super().hello()

class D(B, C):
    def hello(self): print("D"); super().hello()

print([cl.__name__ for cl in D.__mro__]) 

print("Calling D().hello()")
D().hello()


# Why didn't we get "A" printed twice? 
# It is because of the MRO (Method Resolution Order) in Python, 
# which is determined by the C3 linearization algorithm. 
# D(B, c) means the MRO is an ordered queue of classes
# which is D -> B -> C -> A -> object. 

# Here is the chronological order of method calls:
# 1. D().hello() is called, which prints "D" and calls super
# 2. super() in D refers to B, so B().hello() is called, which prints "B" and calls super
# 3. super() in B refers to C, so C().hello() is called 
# 4. super() in C refers to A, so A().hello() is called, which prints "A" and calls super
# 5. super() in A refers to object, which has no hello method, so the call chain ends here.