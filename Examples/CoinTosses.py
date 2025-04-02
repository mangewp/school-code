from Coin import Coin

def main():
    coin1 = Coin()
    coin2 = Coin()
    coin3 = Coin()
    
    print("Three coins with these sides up.")
    print(coin1.get_sideup(), coin2.get_sideup(), coin3.get_sideup())
    print("Tossing all 3 coins.")
    
    coin1.toss()
    coin2.toss()
    coin3.toss()
    
    print("Now here are the sides up.")
    print(coin1.get_sideup(), coin2.get_sideup(), coin3.get_sideup())

if __name__ == "__main__":
    main()