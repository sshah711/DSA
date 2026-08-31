def isPowerOfTwo(n):
    if n == 1:
        return True
    elif n % 2 != 0 or n < 1:
        return False
    return isPowerOfTwo(n / 2)


print(isPowerOfTwo(1))
