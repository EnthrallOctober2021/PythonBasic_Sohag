# Incremental for loop
for a in range(1, 10, 2):
    print(a)

# Decremental for loop
for b in range(10, 1, -2):
    print(b)

print("------ Use of break in for loop ---------")
print("Before use of break the output is below:")
for c in range(1, 20, 3):
    print(c)
print("After use of break the output is below:")
for d in range(1, 20, 3):
    if d ==13:
        break
    print(d)

print("After use of break the output is below:")
for e in range(0, 20, 3):
    if e ==13:
        break
    print(e)

print("\n------ Use of break in While loop ---------")
i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i = i + 1


print("When break implemented, loop stop before that condition\n")

print("------Use of continue in for loop------")
print("Before use of continue the output is below:")
for x in range(1, 20, 3):
    print(x)
print("\nAfter use of continue the output is below:")
for x in range(1, 20, 3): # 4, 10 and 16 will be out
    if x % 2 == 0:
        continue
    print(x)

print("\n------ Use of continue in While loop ---------")
y = 1
while y <= 12:
    if y == 7:
        y=y+2 # this is an special condition to make the loop running
        continue
    print(y)
    y=y+2

print("When condition is met, condition will skip and continue")

print("\n------break---------")
i = 1
while i <= 12:
    if i == 8:  # when i==7 then break works otherwise it goes next step
        break
    print(i)
    i = i + 1  # i++

print("\n------continue---------")

for x in range(1, 20, 3):
    # print(x)
    if x % 2 != 0:  # skipping condition
        continue
    print(x)