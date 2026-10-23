print("=============================================================")
print("       ATM SYSTEM-A Simple ATM Simulation using Python     ")
print("=============================================================")


balance = 10000
pin = 1234

entered_pin = int(input("Enter PIN:"))
if entered_pin == pin:
  while True:
    print("\n1.Check 2.Wihdraw 3.Deposit 4.Exit")
    option = int(input("Select: "))
    if option == 1:
        print(f"Balance: {balance}")
    elif option == 2:
        amount = int(input("Withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Success! Remaining: {balance}")
        else:
           print("Insufficient balance")
    elif option == 3:
        amount = int(input("Deposit: "))
        balance += amount
        print(f"Success New Balance: {balance}")
    elif option == 4:
        print("Thank you!")
        break

else:
    print("Wrong PIN")
        
        
      