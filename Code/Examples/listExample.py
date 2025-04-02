cars = ["ford", "chevy", "bmw"]
#newCar = input("Enter a new input to replace " + cars[1] + ": " )
#cars[1] = newCar
print(cars)
for c in cars:
    print(c)

    
nums = list(range(1,10,2))
print(nums)
for n in nums:
    print(n)
    
print (cars[1])
print (cars[-1])

days = ["sun", "mon", "tues", "wed", "thurs", "fri", "sat"]
midDays = days[2:4]
print(midDays)

def main():
    prodNums = ["V475", "F987", "0143", "R688"]
    search = input("Enter a product number: ")
    
    if search in prodNums:
        print(f'{search} was found in the list.')
    else:
        print (f'{search} was NOT found in the list.')

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

import random
def roll():
    nums = {1,2,3,4,5,6}
    roll = random.choice(nums)
    print(roll)
    
def twoDimensionalList():
    partner = [["Joe", "Kim"], ["Sam", "Sue"], ["Kelly", "Chris"]]
    print(partner)
    print(partner[0])
    print(partner[0][1])
    
twoDimensionalList()