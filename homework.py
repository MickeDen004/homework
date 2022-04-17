class MyString():

    def __init__(self, name):
        self.name = name

    def self_len_count(self):
        return f"Name length: {len(self.name)}"

    def enter_string_count(self, string_value):
        x = len(string_value)
        return x


my_string = MyString("Alyona")
print(my_string.self_len_count())

print(isinstance(MyString, type))


# creating Person Class
class Person:
    person_id = 0
    person_name = ""

    # defining an initializing function
    def __init__(self, personid, personname):
        self.person_id = personid
        self.person_name = personname

        # defining a callable function

    def __call__(self, *args, **kwargs):
        print('Printing Arguments')
        print(*args)

        print('Printing Keyword Arguments')
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))

        # instantiating the class


m = Person(15, 'George')

# printing the object
print(m)

# checking if the object is callable or not
print("The Person object is callable: ", callable)
