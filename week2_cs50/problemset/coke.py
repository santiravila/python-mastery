denominations = [25, 10, 5]
amount_due = 50
change_owed = 0

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in denominations:
        if coin > amount_due:
            change_owed += (coin - amount_due)
        amount_due -= coin
        
print(f"Change Owed: {change_owed}")