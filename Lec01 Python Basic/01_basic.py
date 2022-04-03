import datetime
print(datetime.datetime.now())

# 1: To comment out multiple line, we type /**/ in Java, but in python it is below
"""
Thi is the way to comment out multiple line by 3 double quotation
hi
"""

# 2
print("\n-------------------------------------------------------------")
print("Hello World!")
print('Hey Python')  # single quotation is also ok
print(10 * "Hello World! ")

# 3 (how to Concatenate? 3 way. Which one is the best among first 2?)
print("\n-------------------------------------------------------------")
print("Hello World!" + " " + "concatenation 1st way.")
print("Hello World!", "concatenation 2nd way.")

# 3 (Use of end parameter to Concatenate)
print("\n-------------------------------------------------------------")
print("Hi!", "concatenation 3rd way.", end=" ")
print("I am using end feature here, it will concatenate with the previous line.")

# 4 (use of next line by \n and tab by \t)
print("\n-------------------------------------------------------------")
print("\nI am using new line by using backslash n.\nI am expecting it in new line")
print("I am using backslash t to get the tab option. \tDid you get it? \n\tCan't see the tab yet?")
print("\n")

# 5 (use of only \)
# Printing single and double quote
print("\n-------------------------------------------------------------")
print("\'Tofael\'")  # only back slash tell the program to ignore the next symbol of it.
print('\"Tofael\"')
print('\'Tofael\'')
print('\*Tofael\*')
print("\"Tofael\"")
print("'Tofael'")  # Also possible this way
print('"Tofael"')

print("C:\Windows")
print("C:\'Windows'")

# 6(use of \r)
# never see to use
print("\n-------------------------------------------------------------")
print('Hello Sir!\r 347-653-7214')  # using \r --> return carriage
# \r don't work in Java, why?  # Shohag
