class Demo:
    def __new__(cls):
        print("Inside __new__: object creation")
        obj = object.__new__(cls)
        return obj

    def __init__(self):
        print("Inside __init__: object initialization")


d = Demo()

print("\nManual object creation using object.__new__()")
obj = object.__new__(Demo)
Demo.__init__(obj)


class MyInt(int):
    def __new__(cls, value):
        print("Inside __new__ of MyInt")
        value = value + 10
        return super().__new__(cls, value)

    def __init__(self, value):
        print("Inside __init__ of MyInt")


x = MyInt(5)
print("Final value of immutable object:", x)
