def selectSort(nums):

    for i in range(0,len(nums)):
        minNum = nums[i]
        minNumIndex = i
        for j in range(i, len(nums)):
            if minNum > nums[j]:
                minNum = nums[j]
                minNumIndex = j

        tmpValue = nums[i]
        nums[i] = nums[minNumIndex]
        nums[minNumIndex] = tmpValue

    return nums

nums = [1,3,5,7,9,2,4,6,8,10,0]
print(selectSort(nums))
