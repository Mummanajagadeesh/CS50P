due=50
while True:
    print("Amount Due:",due)
    coin=int(input("Insert Coin:"))
    if coin==25 or coin==10 or coin==5:
        due=due-coin
        if due<=0:
           print("Change Owed:",abs(due))
           break
    else:
       continue
