myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset2 = set([3,4,5])

data = set (['hello', 'goodbye'])
print(data)

myset2.update([5,6,7,8])

print(myset2)
      
#data.clear()

myset.union(myset2)
print (myset)

myset & myset2 #brings back whats common betwwen the two

myset.difference(myset) #or myset - myset2

myset ^ myset2 #systematic_difference