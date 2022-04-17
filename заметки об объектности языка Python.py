# Объекты
# __class__ and __dict__
def foo():
    pass


print(foo.__class__)
print(foo.__dict__)


class A(object):
    qux = 'A'

    def __init__(self, name):
        self.name = name

    def foo(self):
        print('foo')


a = A('a')
print(a.__dict__)
print(a.__class__)
print(type(a))
print(a.__class__ is type(a))
print(a.__class__ is type(a) is A)

# Переопределение класса объекта а


class B(object):
    qux = 'B'

    def __init__(self):
        self.name = 'B object'

    def bar(self):
        print('bar')


print(f'\n{a.__dict__}')
print(a.foo())
print(a.__class__)
a.__class__ = B
print(a.__class__, a.name)

# классовые переменные доступны
print(a.bar())
print(a.qux)


# установка, удаление, поиск атрибутов объектов
# a.x = 1 <==> setattr(a, 'x', 1)
# del a.x <==> delattr(a, 'x')
# a.x <==> getattr(a, 'x')

b = B()
print(b.qux)


class A(object):
    pass

print(dict(B.__dict__))

class Abs(object):
    quz = 'Asa'
    def __init__(self, name):
        self.name = name
    def abbbs(self):
        print('abbs')


class Americana(object):
    say = "us"

    def __init__(self, name):
        self.name = name

    def america(self):
        print("AMERICA")


class My_test(object):

    def __new__(cls):
        obj = super(Americana, cls).__new__(cls)
        print('created object', obj)
        return(obj)

    def __init__(self):
        print('initing object', self)


a = My_test()
print(a.__dir__())
print(a.__class__)


class C(object):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(C, cls).__new__(cls)
        return cls.instance