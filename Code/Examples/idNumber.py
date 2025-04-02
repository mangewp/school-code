def main():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idNumber = input("Enter your ID number: ")
  
    print("Your system login is: ")
    print(getLoginName(first, last, idNumber))
    
def getLoginName(first,last,idNumber):
    set1 = first[0]
    
    if len(last) >= 12:
        set2 = last[0:11]
    else:
        set2 = last[:]
        
    set3 = idNumber[-3:]
    
    loginName = set1 + set2 + set3
    
    return loginName

main()