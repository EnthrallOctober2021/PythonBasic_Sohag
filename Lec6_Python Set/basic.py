print("#creating set.............")
#just using {}
#set1={}
set1={"White","Blue"}
#using set()----constructor method
set2=set() # we are calling method so we use ()


print("#adding obj in set.............")
set2.add("Blue")
set2.add("Blue")# no duplicate----it will not be added
set2.add("Red")
set2.add("Black")
set2.add("Green")
print(set2)  #printing the set

print("#checking item by in keyword in if---else in set.............")
trueOrFalse="Black" in set2

if trueOrFalse==True:
    print(set2)
else:
    print("Dont print the set")

#Using in keyword result directly in if--els code
if "Black" in set2:
    print(set2)
else:
    print("Dont print the set")

print("#checking we cant modify but add new item in set.............")
#we dont have this optoin like lie--------set2[0]="Yellow"  this because unchangeable feature
set2.add("Yellow")
set2.add("Purple")
print(set2)

print("#checking we cant use + operator or add() to add another set but we can use update() in set.............")
#not possible in set--------------->set3=set2+set1
#not possible in set---set3=set2.add(set1)---will show you non hashable
set2.update(set1)   #as we have common item in set1 and set2---->it will ignore duplicate ("Blue") is duplicate
print(set2)

#cheking white is there or not
print("White" in set2)  #before removing
set2.remove("White")#removing---it is checking internaly item is there or not
print("White" in set2)#after removing

print("#using discard()------")
print("Orange" in set2)  #before removing
set2.discard("Orange")#removing --it is not checking internaly item is there or not---not giving error it not present
print(set2)
print("#using pop()------")
#in list
list1=["Yellow","Red"]
print(list1)
# list1.pop(0)
# list1.pop(1)
list1.pop()#in set if we dont pass index number ---then it will remove last item
print(list1)
#now Set------------
#set2.pop(0) #set.pop() takes no arguments (1 given)------> we cant use it in set
print(set2)
set2.pop() #which item we are removing --last item but not which item
print(set2)

#clear()--------------------it will cleare all date in set and give you empty set()---> it is giving empty{}
set3={1,8,9}
print(set3)
set3.clear()
print(set3)
#as it is empty not delted so still we will able to add
set3.add(10)
print(set3)

#if want to delete set----> we use del keyword before set ref
del set3
#print(set3) #giving youo---error----name 'set3' is not defined. Did you mean: 'set1'?

print("# joining-----------------------------------")
#set4=set1+set2----not possible
#set2.add(set1)---not possible

#union---adding items from 2 sets by checking duplicate....like---common+uncommon
set5={5,8,9,10}
set6={5,10,19}
set7=set5.union(set6)
print(set7) #will prin common+uncommon----unique

"""Note----diff btw   update()  and union()--
update()----it will update your set (checking duplicate) and inserting new item in your set
set1.update(set2)--------it is updateing set1 for example before we had in set1= {2,5}  now it is adding new item from set2 
like in we had set2={2,10,8}  --->now in set1={2,5,8,10}
union()----it will give new set (after checking common+uncommon------ not updating your prev set 
set1.union(set2)----now you have to put in new set set3=set1.union(set2). So in new set we have common+uncommon items from set1 and set2
set3={2,8,5,10}
"""

#when we use intersection()-----it will take from both sets only common number---build a new set

set8=set5.intersection(set6)
print(set8)
print(set6)
print(set8)
#when we use symmetric_difference()-----it will take from both sets only uncommon number---build a new set
set9=set8.symmetric_difference(set6)
print(set8)
print(set6)
print(set9)
#some common using approach---
print("#using common useable methods not set specific")
print(len(set9))
print(type(set9))

#converting into set
list5=[5,9,8]
print(list5)
print(type(set9))
#approach 1
set10=set(list5)
print(set10)
#approach 2
set11=set([5,9,8]) #[5,9,8] this is list
print(set11)

#update() for updating set12 with diff data type set13
set12={"Noyon","Sohag"}
set13={5,8,}
set13.update(set12)
print(set13)
