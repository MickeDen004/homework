class A(object):
    pass

# то же самое что и

print(type('A', (object,), {}))

class B(A):
    def foo(self):
        42

print(type('B', (A, ), {'foo': lambda self: 42}))
b = B()
print(b.__dir__())
print(b.foo())

# описк аттрибутов
class Ameta(type):
    def foo(cls):
        print ('Ameta.foo')

class A(object):
    __metaclass__ = Ameta

print(Ameta.foo(A))
class B(A):
    @classmethod
    def foo(cls):
        print('B.foo')

class Meta(type):
    def __new__(mcls, name, bases, attrs):
        print("Creating new class", name)
        return super(Meta, mcls).__new__(mcls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print('Initing new class', name)

class A(object):
    __metaclass__ = Meta

print(A)