# Logical operator --> And, or, not --> When we use more than one condition
# To make program: Largest/smallest Number, Leap year, Vowel/Consonant, Capital/Small
num1 = 9
num2 = 18
num3 = 87
if num1 > num2 and num1 > num3:
    print("num1 is", num1, "and greater than", num2, "and", num3)
elif num2 > num1 and num2 > num3:
    print("num2 is", num2, "and greater than", num1, "and", num3)
else:
    print("num3 is", num3, "and greater than", num1, "and", num2)

# Vowel
myAlphabet = input("Enter any alphabet: ")
if myAlphabet == 'a' or myAlphabet == 'e' or myAlphabet == 'i' or myAlphabet == 'o' or myAlphabet == 'u' or myAlphabet == 'A' or myAlphabet == 'E' or myAlphabet == 'I' or myAlphabet == 'O' or myAlphabet == 'U':
    print(myAlphabet, "is a Vowel")
else:
    print(myAlphabet, "is a Consonant")

# Vowel

# input from user
letter = input('Enter any character: ')
# check vowel or constant and display result
if letter.upper() in ('A', 'E', 'I', 'O', 'U'):
    print(letter, "is a Vowel")
elif letter.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(letter, "is a Vowel")
else:
    print(letter, "is a Consonant")

