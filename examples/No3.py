def linearSearch(nums, value):
    if len(nums) == 0:
        return -1

    i = 0
    for i in range(len(nums)):
        if nums[i] == value:
            return i

    if i >= len(nums)-1:
        return -1


nums = [1,3,5,2,4]
print(linearSearch(nums, 2))
