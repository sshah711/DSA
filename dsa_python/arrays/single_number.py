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


n = [1, 1, 1, 2, 3, 2, 2]
print(singleNumber(n))


#  exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
def singleNumber(nums):
    xor_all = 0

    # Step 1: XOR all numbers
    for num in nums:
        xor_all ^= num

    # Step 2: Find rightmost set bit
    rightmost_bit = xor_all & -xor_all

    x = 0
    y = 0

    # Step 3: Divide into two groups and XOR
    for num in nums:
        if num & rightmost_bit:
            x ^= num
        else:
            y ^= num

    return [x, y]


n = [1, 1, 2, 2, 8, 5]
print(singleNumber(n))
