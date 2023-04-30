def bubbleSort(nums):
    for i in range(0, len(nums)):
        print("==> i=%d" % i)

        for j in range(len(nums) - 1, i, -1):
            print("  ==> j=%d" % j, end="  ")
            if nums[j] < nums[j - 1]:
                k = nums[j]
                nums[j] = nums[j - 1]
                nums[j - 1] = k
            print(nums)

    return nums


nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 0]
print(bubbleSort(nums))
