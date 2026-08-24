def best_time_to_buy_sell_to_get_max_profit(price):
    profit = 0
    min = price[0]
    n = len(price)
    # brute force approach O(n^2)
    # for i in range(n):
    #     for j in range(i, n):
    #         if price[i] < price[j]:
    #             ans = price[j] - price[i]
    #             if profit < ans:
    #                 profit = ans
    # return profit

    for i in range(n):
        if price[i] - min > profit:
            profit = price[i] - min
        if price[i] < min:
            min = price[i]
    return profit


p = [7, 5, 3, 4]
print(best_time_to_buy_sell_to_get_max_profit(p))
