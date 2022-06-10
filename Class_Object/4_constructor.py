#the magic or dunder----__init__() is called constructor
#note-all magic methods prefix and suffix surrounded by double underscore--so called dunder (d=double + under)
class Students:
#    default constructor
    def __init__(self):
        print("Printing from default constructor-----")
# #not possible: if you have 2nd default then 2nd one will work not first one
#     def __init__(self):
#         print("Printing from default constructor-2")

# if we have last constructor parmeterized constructor then as it is last one will work only
#parameterized cons
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Printin from parameterized (2 pram) constructor")

#obj1 = Students()  #creating obj by default constructor----at a time two constructor will not work
obj2=Students("sohag",42) #creating obj by parameterized costructor
print(obj2.name)


##############    NOTE    #####################
''' IN PYTHONON INTERPRETER WILL DETECT ONLY LAST CONSTRUCTOR----DEFAULT OR PARAMETERIZED DOESNT MATTER '''
''' SO AS PER CONSTRUCTOR IF WE NEED HAVE TO PASS VALUE FOR PRAMATER----NOT EXTRA AND NOT LESS'''


