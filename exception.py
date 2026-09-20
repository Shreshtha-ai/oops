class EvenOnly(list):
    def append(self,integer):
        if not isinstance(integer, int):
            raise TypeError("Only Integers can be added")
        if integer %2:
            raise ValueError("Only even numbers allowed")
        super().append(integer)

e = EvenOnly()
e.append(1)
e.append(4)
e.append(6)
print(e)
