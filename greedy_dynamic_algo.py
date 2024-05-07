import timeit

def find_coins_greedy(amount, coins):
    coins.sort(reverse=True)
    coin_count = {}
    for coin in coins:
        coin_count[coin] = amount // coin
        amount %= coin
    return coin_count


def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    result = {}
    i = amount
    for coin in sorted(coins, reverse=True):
        result[coin] = i // coin
        i %= coin
    return result


# Задаємо функції та тести
functions = {
    "Greedy Algorithm": find_coins_greedy,
    "Dynamic Programming": find_min_coins
}

# Вимірюємо час виконання кожної функції
amount = 1000
coins = [50, 25, 10, 5, 2, 1]
for name, func in functions.items():
    time_taken = timeit.timeit(stmt=lambda: func(amount, coins), number=10000)
    print(f"{name}: {time_taken:.6f} seconds")
