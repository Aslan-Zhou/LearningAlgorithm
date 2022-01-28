def factorial1(num):

    retuls = 1
    for i in range(num,1,-1):
        retuls *= i

    return retuls

def factorial2(num):

    if num == 1:

        return 1
    else:

        return num * factorial2(num-1)

print(factorial1(10))
print(factorial2(10))
