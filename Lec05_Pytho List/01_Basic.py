#create a list
list1=[] #empty
#by using list() method ---constructor method
list2=list()#empty
list2.append(5)#now we are adding member in list
print(list2)
myList=[5,50.5,8,9,10,1,100] #having data in list when created
#see the length
print(len(myList))
#adding more
myList.append(88)
myList.insert(1,8888)
#removing member

myList.remove(8888)
myList.pop()#it will remove at end (last item)
myList.pop(0)#it will remove 0 index

print("#lets have ne list-------")
list3=[5,8,9,99,100]
print(list3)
#removing
del list3[0]
#del list3
print(list3)

#clear all
list3.clear() # it will clear all members not list
print(list3)

#check what index
print("check what  index for 10",myList.index(10)) # it will give you index number where 10 is stored

#check in which index
print("check what  in what index ",myList[1])  # we will get the member

#print list only not the value--but value will be shown in []
print(myList)
#print single member by passing index
print(myList[-1])  #  for example weh have myList[5,8,9,10]  if we say -1 it will print top right member means 10
#by using we are printing all members
print("Printing by using loop")
for a in myList:
    print(a)
#if we wnat to remove any member
myList.remove(100)

#we can convert diff colleciotn int to list
myTuple=(5,8,9,88)
print(type(myTuple))
#ccnverting--
myNewList=list(myTuple)
print(type(myNewList))# show you list type
#we can directly pass tuple or other colleciotn type too
list1=list((8,9,9,10,10,10))  #inner () is the touple as we used ()
print(type(list1))
#checking which members occuring max or min
print(max(list1))
print(min(list1))

print("#if we check how many time---the use count()")
print(list1.count(10))

print("#replace member---------------")

#having a list
enSt=list()
enSt.append("Nabila")
enSt.append("Akbar")
enSt.append("Ruhul")
enSt.append("Sohag")
#print(enSt.index("Sohag"))
enSt.append("Noyon")
print(enSt)
enSt[1]="Shamsu"
#print(enSt.index("Shamsu"))
print(enSt)
#change in a range
enSt[1:3]=["Humayun","Amin"]
print(enSt)


#New list for looping
list6=["Amin","Nabila","Shamsu","Sohag","shimul"]
print(list6)

print("#for each looping")
for n in list6:
    print(n)
print("#shorthand looping")
[print(x) for x in list6]

print("#using a range---for loop")
for y in range(0,len(list6),1):
    print(list6[y])


#new list
list7=[5,100,1,10,500]
print(list7)
list7.sort()
print(list7)
#reversing way
list7.reverse()#if we first sort()---it will give you sorted way in asscending order then if you reverse it then ultimately you will ge descending order
print(list7)

list8=["Amin","Nabila","Zayan","Labiba","Simul"]
print(list8)
list8.sort(reverse=True)
print(list8)

print("Cophying-----")
#after copying if any change in prev list in new list no impact
list9=list8.copy()
print(list9)
#lets do some change in prev list
list8[0]="Al-Amin"
print(list8)
print(list9)#still it will carry prev version

#if we assign a list in a new list
list10=list8
print(list10)
#lets do some change in prev list
list8[0]="AminulIslam"
print(list10)

print("#Joining-------------")
list11=["Tofayel"]
list12=list11+list8
print(list12)
# or by using append()
list13=["Lobid"]
print(list13)
list13.append(list12)
print(list13)
list13.extend(list8)
print(list13)


print("Slicing...........")
list15=[5,8,9,12,100,1,50]
print(list15[:5:1]) #if not mentioned---initialized part=0, length pare=total length, inc/dec=+1


print("use in keyword to check in the list")
print(1000 in list15)

print("use + operator to concatinate list------")
list16=list15+[1000]
print(1000 in list16)

print("how we can split string and put in our list------")
sentece="My name,is,zzzzzz"
list17=sentece.split(" ")
print(list17)
print(type(list17))

print("#insert any tuple in lis----------------")
myTuple=(5,6,9)
print(type(myTuple))

list20=[50,80]

list19=[10,15]
print(list19)
list19.insert(1,myTuple)
print(list19)
list19.insert(3,list20)
print(list19)
print("#joing list in str----------------")
newItem=''.join(str(list19))
print(newItem)