#get input from user
num = int(input("Enter a number 1-7. "))

#if the number is between 1 and 7 then input the day of the week
if num == 1:
    print ("Monday")
elif num == 2:
    print ("Tuesday")
elif num == 3:
    print ("Wednesday")
elif num == 4:
    print ("Thursday")
elif num == 5:
    print ("Friday")
elif num == 6:
    print ("Saturday")
elif num == 7:
    print ("Sunday")
#if the number is not in between 1 and 7 then input an error message
else:
    num > 7 or num < 1
    print ("Error. Enter a number between 1 and 7")