#creating a class with some variables not initialized yet
class entrhall_4:
    name=""
    age=""
    phone=""
#throgh cons initialzing the class property----value will be only respect to the obj
    def __init__(self,stName,stAge,phone):
        self.name=stName
        self.age=stAge
        self.phone=phone
#creating obj by passing value
st1=entrhall_4("Noyon",25,64646464)
print(st1.name)
#before we used to do following way---calling the property then assign value
# st1.name="Sohag"
# st1.age=42

#now creating another obj by passing diff value
st21=entrhall_4("Tara",20,6464646)
st21.phone=911
print(st21.phone)

#if we need we can delete particlare obj's propry value
del st21.phone
print("--------------")
print(st21.phone)
#even we can del obj too
# del st21
# print(st21.name)#no more obj

######   NOTE  ##########
"""WHEN WE INITIALZE CLASS PROPERTY IN THE TIME OF CREATING OBJ FOR THE SAME PROPERTY VALUE WILL BE AS PER OBJ"""