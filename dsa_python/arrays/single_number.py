def single_num(n):
    x = 0
    for i in range(len(n)):
        x = x ^ n[i]
        # print(x)
    return x


n = [1, 1, 2, 3, 3, 4, 4, 5, 5]
print(single_num(n))


# every element appears three times except for one, which appears exactly once. Find the single element and return it.

def singleNumber(nums):
        x = 0
        y = 0

        for num in nums:
            x = (x ^ num) & ~y
            y = (y ^ num) & ~x

        return x
n = [1, 1,1, 2,3,2,2]
print(singleNumber(n))