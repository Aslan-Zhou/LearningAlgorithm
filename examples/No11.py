def func1(n,m):
    if n == 0 or m == 0:
        return 0
    else:
        while m != 0 and n != 0:
            if m > n:
                m %= n
            else:
                n %= m
        if n == 0:
            return m
        else:
            return n
def func2(n,m):
    if n == 0 or m == 0:
        return 0
    else:
        pass

print(func1(1112,695))
print(func2(1112,695))
