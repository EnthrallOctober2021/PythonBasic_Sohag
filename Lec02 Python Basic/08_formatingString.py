num1 = 10
num2 = 15
print("sum of num1 and num2 is: ", num1 + num2, "\n")

# To print--> 10+15 = 25
print(f"{num1}+{num2} = {num1 + num2}")  # f for formatted text, {} for internal cal?
print(r"{num1}+{num2} = {num1 + num2}")  # r-->raw
print(r"Hope you understand how the raw works!")  # printed as it is
print(f"Hi, i am going to add {num1}+{num2} = {num1 + num2}")
print(f"Add:{num1}+{num2} = Sum: {num1 + num2}")

# To print-->20+10=30
num3 = 20
num4 = 10
total = num3 + num4
print(f"{num3} + 10 = {total}")  # {} for internal cal of total

# we don't need f if there is no internal value representation
print("20+10=30")  # just a string

# what is the use of r --->raw

# how to print without a  new line
print("Sohag", end=" ")
print(41)

print("# String Format:------format()-------")
# we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where
# the placeholders {} are *** one or more arg

age = 54
phone = 7747405813
sentence = "I am {} and my phone number is {}"
print(sentence.format(age, phone))  # I am 41 and my phone number is 3474005813

# can be used index number to be placed in correct placeholder
txt = "The phone number {1} belongs to Alex Ferguson. His age is {0}"
print(txt.format(age, phone))

print("\n----- Use of format() --- with fraction (f)--------------------")
txt = "Total cost is {price:.4f} dollars!"  # 2f-->.00, if 3f-->.000
print(txt.format(price=49))
print(txt.format(price=49.846587346856483))

