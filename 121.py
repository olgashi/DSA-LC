import sys


def max_profit(prices):
    m_profit = 0
    min_price = sys.maxsize
    for i in range(0, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > m_profit:
            m_profit = prices[i] - min_price
    return m_profit


print(max_profit([7,1,5,3,6,4]))
