def fabonacci1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fabonacci1(n - 1) + fabonacci1(n - 2)


def fabonacci2(n):
    result1 = 0
    result2 = 1
    print(0, end=', ')
    print(1, end=', ')
    for i in range(n, 2, -1):
        if result1 < result2:
            result1 += result2
            print(result1, end=', ')
        else:
            result2 += result1
            print(result2, end=', ')

    return result1 if result1 > result2 else result2


print(fabonacci1(10))
print(fabonacci2(5555))
