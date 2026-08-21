def palindrom(n):
    copyn=n
    rev = 0
    # last digit (reminder) n%10
    # remove last digit n/10
    if n == 0:  # corner case
        return True
    # n = abs(n)  # corner case

    while (n > 0):
        rem = n % 10
        rev = 10 * rev + rem
        n = n // 10

    print(rev)
    return rev == copyn


n = 1221

print(palindrom(n))




def is_palindrome_fast(n):
    s = str(n)
    print(s[::-1])
    return s == s[::-1]

print(is_palindrome_fast(127210)) 