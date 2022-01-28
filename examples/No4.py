import math

def binarysearch(value,nums):
    if len(nums) == 0:
        return -1

    nums.sort()

    left = 0
    right = len(nums) - 1
    m = math.floor((left + right) / 2)

    while value != nums[m]:
        if value > nums[m]:
            left = m
            m = math.floor((left + right) / 2)
        elif value < nums[m]:
            right = m
            m = math.floor((left + right) / 2)
        if m == left:
            return -1
    if value == nums[m]:
        return m


nums = [1,2,7,8,12,14,17,19,20,25,30,32]
print(binarysearch(13,nums))
