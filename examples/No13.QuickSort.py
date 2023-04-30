def quickSort1(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    same = []
    less = []
    greater = []

    for i in range(0, len(nums)):
        if nums[i] > pivot:
            greater.append(nums[i])
        elif nums[i] == pivot:
            same.append(nums[i])
        else:
            less.append(nums[i])

    return quickSort1(less) + same + quickSort1(greater)


print(quickSort1([3, 5, 8, 1, 2, 9, 4, 7, 6, 3, 5, 8, 1, 2, 9, 4, 7, 6]))
