from curses.ascii import isdigit


digit = input("input a number ")
    
#'digit.isdigit' can also work
if isdigit(digit):
    print("its a digit")
else:
    print("not a digit")
    
values = "one$two$three$four"
print(values.split("$"))