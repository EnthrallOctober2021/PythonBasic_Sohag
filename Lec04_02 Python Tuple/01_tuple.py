"""
 python data type --
 text type: str
 numeric type: int, float, complex
 sequence type: list, tuple, range
 mapping type: dict
 set type: set, frozenset
 boolean type: bool
 binary type: bytes, byte array, memory view

 """

"""
Tuple is another form of collection where different type of data can be stored.
It is similar to list where data is separated by commas. Only the difference is that 
list are enclosed in square bracket and tuple are enclosed in parenthesis.
Tuples cannot be changed, tuple is immutable. But list is mutable, can be changed 
"""

print("\n----- Use of Tuple01 -----")
tp01 = ('Raven', 100, 60.4, 'Davis')  # mixed of different type of data
tp02 = (34, 190, 60.4, 56, 67, 87)  # mixed of different type of data
tp03 = (14, 190, 60, 6, 7, 87)

print(tp01)
print(type(tp01))
print(tp01, type(tp01))  # we also can write them together

print("Length of the tuple: ", len(tp01))
# print("Maximum of the tuple: ", max(tp01)) # Mixed data type, '>' not supported between instances of 'int' and 'str'
print("Maximum of the tuple: ", max(tp02))
print("Minimum of the tuple: ", min(tp03))

print("\n----- List turned into Tuple elements --------")
aList = [123, 'xyz', 'zara', 'abc']
print("Printing the List: ", aList, type(aList))
aTuple = tuple(aList);
print("List turned into Tuple elements : ", aTuple, type(aTuple))

print("\n----- Tuple Indexing -----")
tp01 = ('Raven', 100, 60.4, 'Davis')  # mixed of different type of data
print(tp01[0])
print(tp01[1])
print(tp01[2])
print(tp01[-1])
print(tp01[-2])
print(tp01[-4])
# Like lists, the tuple elements can be accessed in both the directions. The right most element (last) of the tuple can
# be accessed by using the index -1. The elements from left to right are traversed using the negative indexing.

print("\n----- Tuple slicing  -----")
# It's include all: Initialized block, conditional block, incremental/decremental [+1] block
print(tp01[:])
print("\n")

# It's indicate Initialized block only, by default conditional block [<length, here<4], incr/decr [+1] block is applied
print(tp01[0:])
print(tp01[1:])
print(tp01[2:])
print(tp01[3:])
print("\n")

# It's indicate conditional block only, by default Initialization block [index 0], incr/decr [+1] block is applied
print(tp01[:4])
print(tp01[:3])
print(tp01[:2])
print(tp01[:1])
print("\n")

# It's indicate Initialized and conditional block, by default incr/decr [+1] block is applied
print(tp01[0:4])
print(tp01[0:3])
print(tp01[0:2])
print("\n")

print(tp01[1:4])
print(tp01[1:3])
print(tp01[1:2])
print("\n")

print(tp01[2:4])
print(tp01[2:3])
print(tp01[2:2])
print("\n")

print("\n----- Use of for loop in Tuple01  -----") # TODO: is it for loop or for each loop? need to know
tp01 = ('Raven', 100, 60.4, 'Davis')
for i in tp01:
    print(i)

print("\n----- Use of Tuple04 -----")
tp04 = (("Sohag", 41, "Woodside"), "Orfat", "Tofael")  # Tuple inside a tuple is also possible
print(tp04)

print("\n------------ Tuple Concatenation ------------")
# Concatenation: It concatenates the tuple mentioned on either side of the operator.
tp = tp01 + tp02 + tp03 + tp04
print(tp)

print("\n----- Use of for loop in sum of Tuple  -----")
for j in tp:
    print(j)


print("\n----- Use of Tuple without parentheses -----")
tp10 = 'Raven', 100, 60.4, 'Davis', 'Mohammad'  # tuple might not contain parentheses
print(tp10[0])
print(tp10[-1])
print(tp10[-2])
print(tp10[0], tp10[-1], tp10[2], tp10[-2])
print(tp10[0], tp10[-1], tp10[2], tp10[-2], sep=' | ')

print("\n----- Use of if else loop in Tuple -----")
tp01 = ('Raven', 100, 60.4, 'Davis')
tp10 = 'Raven', 100, 60.4, 'Davis', 'Mohammad'

if tp01 == tp10:
    print("Values of tp1 and tp10 are equal")
else:
    print("Values of tp1 and tp10 are not equal")

print("\n----- Use of unpacking in Tuple -----")
# Unpacking or Multiple assignment
tp10 = 'Raven', 100, 60.4, 'Davis', 'Mohammad'
print(tp10)
a, b, c, d, e = tp10  # you define them with single letter variable  # number can't use
print(a, b, c, d, e)
print(a, c, e)
print(a, b, c, d, e, sep=' | ')

a, b, c, _, _ = tp10  # if we want to unpack few of it, we need to put underscore instead
print(a, b, c, sep=' | ')

a, _, c, _, e = tp10  # if we want to unpack few of it, we need to put underscore instead
print(a, c, e, sep=' | ')
print(a, c, e)
