print("------------ How to print multi-line string ------------")
# use '''-----'''  or """------""" line will be printed as given in code
s = '''My name is Alex
I live at woodside, NY, USA.
My neighbourhood is really very convenient to live at.'''
print(s)

print("--------------------------------")
# Strings are Arrays-->strings in Python are arrays of bytes representing unicode characters.
# In python there is no char type --> a single character of a string is a string with length of 1
# we can use [] and index in it to access element of the string
s = "Sohag"
print("s[0] =", s[0])

print("---------- Slicing(Sub-String) ----------")
# -->return a range of characters by using the slice syntax.

print("s[0:3] =", s[0:3])  # Soh    0 to 2 index

# Negative Indexing --> negative indexes to start the slice from the end of the string:
print(s[-1])
# s[0]="S" s[1]="o" s[2]="h" s[3]="a" s[4]="g"
# s[-1]="g" s[-2]="a" s[-3]="h" s[-4]="0" s[-5]="S"
s = "Alex Ferguson"
print(s[-5])
print(s[0])
print(s[0:3])  # [3] exclude-->upper boundary excluded
print(s[-8:-2])  # [-1] exclude-->upper boundary excluded
print("s[-8:-2] =", s[-8:-2])

print("----------- strip() functions ---------------")
# strip() method removes any leading and trailing whitespace
s1 = "     My Name is Alex     Ferguson     "
print(s1)
print(s1.strip())  # similar like Java trim()

# replace() method replaces a string with another string
m = "My NAme Is Alex Ferguson"
print(m.replace("A", "C"))  # will replace all A to C. Case sensitive

text = "My Name Is Alex Ferguson 41"
print("Alex" in text)
print("Blex" in text)
print("Dlex" not in text)

# split() method splits the string into substrings if it finds instances of the separator
x = text.split(" ")
print(x)  # so now strings are splitted into 4 indexes
print(x[3])  # Sohag
