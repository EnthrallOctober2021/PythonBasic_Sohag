# https://www.javatpoint.com/python-tuples
print("\n------------ Tuple ------------")
tuple01 = (4, 8, 3)
tuple03 = (9, 2, 7)
print(tuple01)
print(tuple03)

print("\n------------ Tuple Repetition ------------")
# Repetition: The repetition operator enables the tuple elements to be repeated multiple times.
print(tuple01 * 3)

print("\n------------ Tuple Membership ------------")
# Membership: It returns true if a particular item exists in the tuple otherwise false.
print(4 in tuple01)
print(1 not in tuple01)
print(4 in tuple03)
print(3 not in tuple03)

print("\n------------ Nesting tuple in list ------------")
Employees = [(101, "Adam", 22), (102, "john", 29), (103, "james", 45), (104, "Ben", 34)]
for i in Employees:
    print(i)

Employees[0] = (110, "David", 22)  # this is a LIst, list is mutable, we changed the fist tuple inside List
print("\n------------ Printing list after modification ------------")
for i in Employees:
    print(i)

# not possible line 31, because tuple is immutable
# tuple03 = (9, 2, 7)
# tuple03[0] = 10
# print(tuple03)

"""
Unlike lists, the tuple items can not be deleted by using the del keyword as tuples are immutable.
To delete an entire tuple, we can use the del keyword with the tuple name.
"""
print("\n-----------------------");
tuple = (1, 2, 3, 4, 5, 6, 'physics', 'chemistry', 1997, 2000)
# If we change tuple to tp, the whole execution doesn't work, need to check why?
print(tuple)
# Remove hash from 43-44 and check the error message
# del tuple[0]  # TypeError: 'tuple' object doesn't support item deletion
# print(tuple)

del tuple
print("-----------------------------------------")
# TODO NOT CLEAR, have to see again
print(tuple)  # See the outcome from this, not clear
print("-----------------------------------------")
print(type(tuple))  # See the outcome from this, not clear
"""
1. Using tuple instead of list gives us a clear idea that tuple data is constant and must not be changed.

2. Tuple can simulate dictionary without keys. Consider following nested structure which can be used as a dictionary.
[(101, "John", 22), (102, "Mike", 28),  (103, "Dustin", 30)]  

3. Tuple can be used as the key inside dictionary due to its immutable nature.
"""