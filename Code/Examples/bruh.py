def main():
    try:
        num = float(input("Enter a number or string " + "but only a number will be accepted: "))
        print("ACCEPTED: A number was entered.")
        print("The end.")
        
    except ValueError:
        print("Only a number will be accepted.")
        
    
main()