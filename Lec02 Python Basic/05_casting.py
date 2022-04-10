print("# 1 Why we need Casting\n")
a = '5'
b = '10'
print(a, b)  # 5 10
# When we use coma separated, Any type of Variable is presenting side by side with a space, no concatenation
print(a + b)  # 510
# Here is a complete concatenation without space for similar type of variable, here String + String

a = 5
b = 10
print(a, b)  # 5 10
print(a + b)  # 15
# Here is a complete concatenation without space for similar type of variable, here int + int

a = 5
b = '10'
print(a, b)  # 5 10
# print(a+b)
# The above line is not working as int and String can't be concatenated
# We can solve this problem by casting
print("\n")

print("# 2 Use of Casting\n")
a = '5'
b = '10'
print(a, b)
print(int(a) + int(b))

a = '5.6'
b = '10.7'
print(a, b)
print(float(a) + float(b))  # why 16.299999999999997 ?? float contain 15-16 value after decimal

a = 5
b = 10
print(a, b)
print(str(a) + str(b))  # 510

a = 5
b = '10'
print(a, b)  # 5 10
print(a + int(b))
print("We can cast (int to String), (String to int) etc by the above way\n")

# 3 --- before typecasting
num1 = input("Enter First Number: ")  # input always presented as string type
num2 = input("Enter Second Number: ")  # input always presented as string type

result1 = num1 + num2
print("before Typecasting: " + result1)

# 4 --- after typecasting
result2 = int(num1) + int(num2)
print("After typecasting ", result2, "\n")

# 5 typecast with the input function from the beginning
num1 = int(input("Enter third Number: "))
num2 = int(input("Enter fourth Number: "))

result3 = num1 + num2
print("After Typecasting: ", result3)