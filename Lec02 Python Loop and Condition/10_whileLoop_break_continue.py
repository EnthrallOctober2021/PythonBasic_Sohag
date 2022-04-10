print("\n------ Use of break in While loop ---------")
i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i = i + 1

print("When break implemented, loop stop before that condition\n")

print("\n------ Use of continue in While loop ---------")
y = 1
while y <= 12:
    if y == 7:
        y = y + 2  # this is an special condition to make the loop running
        continue
    print(y)
    y = y + 2

print("When condition is met, condition will skip and continue")

print("\n------break---------")
i = 1
while i <= 12:
    if i == 8:  # when i==7 then break works otherwise it goes next step
        break
    print(i)
    i = i + 1  # i++


