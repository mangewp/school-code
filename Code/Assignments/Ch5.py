#show the conversion to miles
def main():
    showMiles()
  
#get kilometers from user 
def showMiles():
    kilometers = float(input("Enter a number in kilometers to get miles. "))
    miles = (kilometers * 0.6214) 
    print(f'{miles:.2f} miles.')
   
main()