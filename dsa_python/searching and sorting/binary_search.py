def binary(nums, x):
    l = 0
    r = len(nums) - 1

    while r >= l:
        mid = (r + l) // 2

        if x == nums[mid]:
            return mid
        elif x > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


# a = [2, 3, 5, 6, 8, 9, 10]
a = [20, 22]
print(binary(a, 22))
