
def coinChange(coins,total):
    answer = []
    coins = sorted(coins,reverse=True)
    while True:


        for coin in coins:
            if coin <= total:
                answer.append(coin)
                total-=coin
                break

        if total == 0:
            break

        if coins[-1] > total:
            print("Not possible")
            return

    print(answer)

# coins = [1,5,10,20,50,1000]
coins = [1000,50,20,10,5]

total= 2039

coinChange(coins,total)