import bankaccount

def main():
    start_bal = float(input("Enter starting balance: "))
    savings = bankaccount.BankAccount()#start_bal
    
    pay = float(input("How much to deposit: "))
    print("I will deposit that amount in your account.")
    savings.deposit(pay)
    print(f"Your balance is ${savings.get_balance():, .2f}.")
    
    cash = float(input("How much to withdraw: "))
    savings.withdraw(cash)
    print(f"Your new balance is ${savings.get_balance():, .2f}.")
    
if __name__ == "__main__":
    main()