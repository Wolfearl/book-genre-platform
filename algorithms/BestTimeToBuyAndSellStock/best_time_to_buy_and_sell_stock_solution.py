"""
Условие: Найти максимальную прибыль от покупки и продажи акций
Подход: One pass с отслеживанием минимальной цены
Сложность: O(n) по времени, O(1) по памяти
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


# Тесты
if __name__ == "__main__":
    # Test Case 1
    prices1 = [7,1,5,3,6,4]
    print(f"Max Profit: {maxProfit(prices1)}")  # 5
    
    # Test Case 2
    prices2 = [7,6,4,3,1]
    print(f"Max Profit: {maxProfit(prices2)}")  # 0