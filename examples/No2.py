def func(prices):
    if len(prices) <= 1:
        return 0
    else:
        array = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    array.append(0)
                else:
                    array.append(prices[j] - prices[i])

        array.sort()
        price = array.pop()
        return price


prices1 = [1, 2, 7, 3, 9]
print(func(prices1))
prices2 = [2, 2, 1, 4, 3]
print(func(prices2))
prices3 = [1, 7, 3, 9, 6]
print(func(prices3))
prices4 = [9, 8, 7, 6, 5]
print(func(prices4))
prices5 = [9, 7, 6, 15]
print(func(prices5))
