class student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age


c = student("abc",9)

print(c.name)
print(c._student__age)