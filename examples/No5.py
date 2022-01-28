def findMinNum(nums):
    if len(nums) == 0:
        return None

    minNum = nums[0]
    for i in range(len(nums)):
        if minNum > nums[i]:
            minNum = nums[i]
    return minNum

def findMaxNum(nums):
    if len(nums) == 0:
        return None

    maxNum = nums[0]
    for i in range(len(nums)):
        if maxNum < nums[i]:
            maxNum = nums[i]
    return maxNum

def findMinValueIndex(nums):
    if len(nums) == 0:
        return None

    minNum = nums[0]
    minNumIndex = 0
    for i in range(len(nums)):
        if minNum > nums[i]:
            minNum = nums[i]
            minNumIndex = i
    return minNumIndex

def findMaxValueIndex(nums):
    if len(nums) == 0:
        return None

    maxNum = nums[0]
    maxNumIndex = 0
    for i in range(len(nums)):
        if maxNum < nums[i]:
            maxNum = nums[i]
            maxNumIndex = i
    return maxNumIndex

def avg(nums):
    if len(nums) == 0:
        return None

    sum = 0
    for i in range(len(nums)):
        sum += nums[i]

    avgNum = format(sum /len(nums), '.2f')
    return avgNum

def function(aNums):
    if len(aNums) == 0:
        return None

    avgNum = avg(nums)
    print("In function ==> ", avgNum)

    bNums = []
    for i in range(len(aNums)):
        bNums.append(round(abs(aNums[i] - float(avgNum)), 2))
    print("In function ==> ", aNums)
    print("In function ==> ", bNums)

    minValueIndex = findMaxValueIndex(bNums)
    print("In function ==> ", minValueIndex)

    return aNums[minValueIndex]


nums = [2,7,4,5,8,1,9,3,6,11,12]
print(findMinNum(nums))
print(findMaxNum(nums))
print(avg(nums))
print(function(nums))

