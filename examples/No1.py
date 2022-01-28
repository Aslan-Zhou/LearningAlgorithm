def func(nums):
    nums.sort()

    if len(nums) == 0:
        print("[]")
        return 0
    else:
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                nums[slow + 1] = nums[fast]
                slow += 1
            fast += 1

        print("[", end='')
        for i in range(0,slow + 1):
            print(nums[i], end=',')
        print("]  {}".format(slow + 1))
        return slow + 1

a = []
b = [1,2,3,4,5]
c = [7,4,9,1,4,2,4]
aa = func(a)
bb = func(b)
cc = func(c)
