def main():
    print("Enter a name of 3 superheroes")
    hero1 = input("Superhero 1: ")
    hero2 = input("Superhero 2: ")
    hero3 = input("Superhero 3: ")
    
    myfile = open("superhero.txt", "a")
    myfile.write(hero1 + "\n" )
    myfile.write(hero2 + "\n" )
    myfile.write(hero3 + "\n" )
    
    myfile.close()
    print("Names were written to the superheroes.txt file.")
    
main()