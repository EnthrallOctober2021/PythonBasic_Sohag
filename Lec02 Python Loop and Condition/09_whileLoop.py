print("----- Use of While Loop 01 -----\n")
i = 1
while i < 5:
    print(i)
    i = i + 1  # we can also write i+=1

print("----- Use of While Loop 02 -----\n")
i = 0
while i <= 10:
    print(i)
    i = i + 2

print("----- Use of While Loop 03 -----\n")
# calculate the sum of all even numbers from 0-10
i = 0
total = 0
while i <= 10:
    total = total + i
    i = i + 2
print("sum of all even numbers:", total, "\n")

# sum of numbers
n = int(input("Enter the range of the loop: "))
total = 0
i = 1
while i <= n:
    total = total + i
    i = i + 1
print("sum of all even ad odd numbers:", total)