import math

def showSquare(num):
    sqRoot = math.sqrt(num)
    print(f"The square root of {num} is {sqRoot}")
    print("pi is , ", str((math.pi)))
          
def getNum():
    num = float(input("Enter a number: "))
    return num
    
def showPi(num):
    area = math.pi * num ** 2
    print(f"The area of a circle with a radius of {num} is {area}")