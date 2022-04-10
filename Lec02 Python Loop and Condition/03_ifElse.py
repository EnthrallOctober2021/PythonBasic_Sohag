# if else condition (not Ternary operator)
num1 = 20
num2 = 30
if num1 > num2:
    print("num1 is greater than num2")
elif num1 == num2:
    print("num1 is equal to num2")
elif num1 < num2:
    print("num1 is shorter than num2")

# Alternate way below
# Called Ternary operator -- Ternary means 3
print(num1 if num1 > num2 else num2)

# using input()
var1 = 34
print("please put a number:")
var2 = int(input())

if var2 > var1:
    print("var2 is greater than var1")
else:
    print("var2 is smaller than var1")

