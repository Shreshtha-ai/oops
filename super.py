class A:
    def __init__(self):
        print("A constructor called")

class B(A):
    def __init__(self):
        
        print("B constructor called")
        super().__init__()


class C(B):
    def __init__(self):
       
        print("C constructor called")
        super().__init__()


c = C()
print(C.mro()) 

