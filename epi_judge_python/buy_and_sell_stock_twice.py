from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    # TODO - you fill in here.

    n = len(prices)
    if n < 2:
        return 0

    maxProfit = [0 for i in range(n)]

    minSofar = prices[0]
    for i in range(1, n):
        maxProfit[i] = max(maxProfit[i-1], prices[i]-minSofar)
        minSofar = min(minSofar, prices[i])

    maxProfitReverse = [0 for i in range(n)]
    maxSofar = prices[-1]

    maxCombinedProfit = maxProfit[-1]
    for i in range(n - 2, 0, -1):
        maxProfitReverse[i] = max(maxProfitReverse[i+1], maxSofar-prices[i])
        maxSofar = max(maxSofar, prices[i])
        maxCombinedProfit = max(maxCombinedProfit, maxProfitReverse[i] + maxProfit[i-1])

    return maxCombinedProfit

    return 0.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
