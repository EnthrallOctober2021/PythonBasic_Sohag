#create a class
class Student:
    school_name="EnthrallIT"

#without creating obj---by the class name
print(Student.school_name)

#creating obj
# in java we use new followed by class namea and ()/constructor
# in python---will use class name followed by()
noyon=Student() # dont need to mention any type (we do in java)

#calling propery by reference variable
print(noyon.school_name)
#2nd obj and calling property
sohag=Student()
print(sohag.school_name)

