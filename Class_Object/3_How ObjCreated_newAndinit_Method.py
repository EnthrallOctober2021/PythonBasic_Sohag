#when we create obj---internally __init__ magic method is called-----__init__method again call __new__ method
class Student:

#obj is being created
    def __new__(cls, *args, **kwargs):
        print("obj is being created")

#obj is being initialized
    def __init__(self):
        print("obj is being initialized")

obj1 =Student()

#note: if comment out __new__ method code---then you will see __init__method statement
# otherwise only __new__method statement will print

