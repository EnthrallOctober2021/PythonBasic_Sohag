myCar={"make":"Nissan","Model":"Rogue","year":2016}

print(myCar["make"])
allKeys=myCar.keys()
allValues=myCar.values()

print("Kyes:",allKeys)
print("Vlues:",allValues)

for x in allKeys:
    print(x,": ",myCar[x])

