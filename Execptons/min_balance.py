class MinBalance(Exception):
    pass

acc_balance = 10000
def withdraw(amount):
    global acc_balance
    if acc_balance - amount < 5000:
        raise MinBalance("You cannot withdraw")
    elif acc_balance - amount >= 5000:
        acc_balance = acc_balance - amount
        return acc_balance


amount = int(input("enter the withdrawal amount"))
try:
    balance = withdraw(amount)
    print("balance is", balance)
except MinBalance as e:
    print(e)
finally:
    print("your transaction is complete")

