#define the main function
def main():
    readLine()
    
#read a maximum of 5 lines
def readLine():
    file = input('Enter a file name with its file extension: ')
    objectFile = open(file, 'r')
    line = objectFile.readline()
    line = line.rstrip('\n')
    count = 0
    while count <= 4:
        if line == '' :
            count += 5
        else:
            print(line)
            line = objectFile.readline()
            line = line.rstrip('\n')
            count += 1
    objectFile.close()
    
#runs the main function
main()