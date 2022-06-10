
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
# How to Print single and double quote
print("---------- Escape Character by \ ------------")
# we use backslash to skip coming up char or special char  ->for example "" inside ""
print("\'Tofael\'")  # only backslash tell the program to ignore the next symbol of it.
print('\"Tofael\"')
print('\'Tofael\'')
print('\*Tofael\*')
print("\"Tofael\"")
print("'Tofael'")  # Also possible this way
print('"Tofael"')

print("C:\Windows")
print("C:\'Windows'")

tex1 = 'It\'s alright now'
print(tex1)

# 6(use of \r)
# never see to use
print("\n-------------------------------------------------------------")
print('Hello Sir!\r 347-653-7214')  # using \r --> return carriage
# \r don't work in Java, why?  # Shohag

# for new line we use \n
print("New\nLine")

# for Carriage Return we use \r
print("Carriage\rReturn")

# for tab we use \t
print("Tab\tTab")  # Tab Tab

# for Backspace we use \b
print("Back \bSpace")  # BackSpace

# for Form Feed we use \f
print("Form \fFeed")

# for Octal value we use \ooo
# A backslash followed by three integers will result in a octal value:
txt = "\150\105\154\154"
print(txt)  # hEll

# for Hex value we use \xhh
# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
