from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.

    minSoFar = float("inf")
    maxGain = 0

    for price in prices:
        if price - minSoFar > maxGain:
            maxGain = price - minSoFar

        if price < minSoFar:
            minSoFar = price

    return maxGain


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
