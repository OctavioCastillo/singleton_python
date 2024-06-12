class MetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            """ Check if instance already exists """
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class A(metaclass=MetaClass):

    def __init__(self):
        pass

obj1 = A()
print(id(obj1))

obj2 = A()
print(id(obj2))

print(obj1 is obj2)