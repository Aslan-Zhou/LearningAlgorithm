def insertionSort(nums):
    for i in range(1, len(nums)):
        print("==> i=%d, " % i, nums)

        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                tmpValue = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = tmpValue
            else:
                break
    return nums


nums = [5,3,4,7,2,8,6,9,1,]
print(insertionSort(nums))
