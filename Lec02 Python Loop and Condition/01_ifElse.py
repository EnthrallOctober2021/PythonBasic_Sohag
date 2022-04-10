# get accepted or denied return by using if twice, but not a good practice
Age = 41
if Age >= 18:
    print("Accepted for driving test")
if Age < 18:
    print("Denied for driving test")

# by using if else
if Age >= 18:
    print("Accepted for driving test")
else:
    print("Denied for driving test")

# another example by using if else
num1 = 10
num2 = 15

if num1 >= num2:
    print(num1)
else:
    print(num2)

# Even/Odd
num = int(input("Enter the number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
