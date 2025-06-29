def main():
    netflix = ["abc","def","ghi"]
    for n in range(len(netflix)):
        print (netflix[n])
    newMovie = input("Enter a new input to replace " + netflix[1] + ": " )
    netflix[1] = newMovie
    print(netflix)
    

def poop():
    myList = [10,20,30,40]
    index = 0
    while index < len(myList):
        print(myList[index])
        index += 1
    
    names = ["jenny", "kelly", "Chole", "Aubrey"]
    for index in range(len(names)):
        print(names[index])

def names():
    nameList = []
    
    again = "y"
    
    while again == "y":
        name = input("Enter a name: ")
        nameList.append(name)
        again = input("Do you want to add another name? (y/n): ")
        print()
        
    print("Here are the names you entered. ")
    
    for name in nameList:
        print(name)
        
    #Sort
    nameList.sort()
    print('Sorted: ', nameList)
    print()
    
    #Index
    index = nameList.index("John")
    print("Index for John: ", index)
    print()
    
    #Insert Item
    newName = input("Enter a name to insert at the beginning: ")
    nameList.insert(0, newName)
    print(nameList)
    print()
    
    #Remove an Item
    removeName = input("Enter a name to remove: ")
    nameList.remove(removeName)
    print(nameList)
    print()
    
    #Reverse Order
    nameList.reverse()
    print(f"Reversed: {nameList}")
    print()
    
    #Delete by Index
    getIndex = int(input("Enter an index between 0 and {len(nameList) - 1}: "))
    del nameList[getIndex]
    print(f'Deleted by index {nameList}')
    print()
    
    #Min and max numbers
    nums = [10, 4, 279, 3, 56, 9]
    print("Here are a list of Numbers. ")
    print(f"Lowest: {min(nums)}.")
    print(f"Highest: {max(nums)}.")
names()