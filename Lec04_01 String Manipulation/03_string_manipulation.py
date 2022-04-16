"""
Some String Methods:
capitalize()Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()     Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()Sets the tab size of the string
find()	    Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	    Joins the elements of an iterable to the end of the string
ljust()	    Returns a left justified version of the string
lower()	    Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind() 	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	    Returns a right justified version of the string
rpartition()Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	    Splits the string at the specified separator, and returns a list
splitlines()Splits the string at line breaks and returns a list
startswith()Returns true if the string starts with the specified value
strip()	    Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	    Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	    Converts a string into upper case
zfill()	    Fills the string with a specified number of 0 values at the beginning
"""

print("\n----- Use of center() -- after how many space the word will start.-----")
txt = "Manhattan"
print(txt.center(35))  # the text size + left white space + right white space

print("\n----- Use of expandtabs() --- how many spaces between tabs -----")
txt = "H\te\tl\tl\to"
x = txt.expandtabs(10)
print(x)

print("\n----- Use of find() --- to find the position of any letter or words-----------------------------")
# finds the first occurrence of the specified value.
# almost the same as the index()--But index() method raises an exception and find() returns -1 if not found
txt = "My name is "
y = txt.find("J")
print(y)  # Will not throw Exception if it is absent, rather returns -1
y = txt.find("z")
print(y)  # Will not throw Exception if it is absent, rather returns -1

print("\n----- Use of index() --- to find the position of any letter or words")
txt = "My name is Alex J Joey"
x = txt.index("A")
print(x)
# y = txt.index("Z") # ValueError: substring not found
# print(y)  # Will throw Exception if it is absent

print("\n----- Use of ljust() -----")
# Returns a left justified version of the string
txt = "S"
x = txt.ljust(5, "o")  # Total 5 including the txt, txt will be on most left then what you want to add will be on right
print(x)
print(x, "des ne.")   # Meaning ---> Soooo des ne? --> Really? in japanese
# left justified version of the word "Soooo" -->between first char "S" and next str "o"

print("\n----- Use of rjust() -----")
# Returns a right justified version of the string
txt = "K"
y = txt.rjust(5, "O")  # Total 5 including the txt, txt will be on most right then what you want to add
print(y)
print(y, "Got it")
# right justified version of the word "OOOOK" -->between last char "K" and previous str "O"

print("\n----- Use of zfill() -----")
# Fill the string with zeros until it is nth (here 7) characters long
txt = "56"
x = txt.zfill(7)
print(x)  # 0000056