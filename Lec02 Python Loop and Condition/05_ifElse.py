# Letter grade
marks = int(input("Please Enter your marks here: "))
if 80 <= marks <= 100:  # chained comparison
    print("A+")
elif 70 <= marks <= 79:
    print("A")
elif 60 <= marks <= 69:  # 2 different way to write
    print("A-")
elif 50 <= marks <= 59:
    print("B+")
elif 40 <= marks <= 49:
    print("B")
else:
    print("F")

# You can drive or not in the USA?
print("Tell me what is your age? ")
age = int(input())
if age < 18:
    print("You can't get a license here in USA")
elif 18 <= age <= 21:
    print("You can get a Junior license and can drive with an assistance")
elif age > 21:
    print("You can legally drive in USA independently")
